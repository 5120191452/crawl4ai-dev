"""SQLite catalog builder and read-only query store."""

from __future__ import annotations

import json
import os
import re
import sqlite3
import tempfile
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .models import Document, Interface
from .parser import parse_snapshot


SCHEMA_VERSION = "1"


def _validate_snapshot(snapshot_dir: Path) -> dict[str, Any]:
    manifest_path = snapshot_dir / "manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"抓取清单不存在: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not manifest.get("complete"):
        raise ValueError("拒绝索引不完整的 Orion Ark 抓取快照")
    if manifest.get("expected_count") != manifest.get("success_count"):
        raise ValueError("抓取成功页数与 Sphinx 索引页数不一致")
    return manifest


def _latest_release(documents: Iterable[Document]) -> tuple[str, str]:
    release = next((doc for doc in documents if doc.docname == "Release Note"), None)
    if not release:
        return "unknown", ""
    match = re.search(r"^##\s+V([^\s]+)(?:\s+(\d{4}-\d{2}-\d{2}))?", release.content, re.MULTILINE)
    return (match.group(1), match.group(2) or "") if match else ("unknown", "")


def _create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode = DELETE;
        PRAGMA foreign_keys = ON;

        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE documents (
            docname TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            source_url TEXT NOT NULL,
            local_path TEXT NOT NULL,
            crawled_at TEXT NOT NULL,
            content TEXT NOT NULL
        );

        CREATE TABLE interfaces (
            id INTEGER PRIMARY KEY,
            symbol TEXT NOT NULL,
            short_name TEXT NOT NULL,
            kind TEXT NOT NULL,
            component TEXT NOT NULL,
            module TEXT NOT NULL,
            class_name TEXT,
            signature TEXT NOT NULL,
            summary TEXT NOT NULL,
            parameters TEXT NOT NULL,
            returns_text TEXT NOT NULL,
            examples TEXT NOT NULL,
            source_url TEXT NOT NULL,
            source_anchor TEXT NOT NULL,
            docname TEXT NOT NULL REFERENCES documents(docname),
            visibility TEXT NOT NULL,
            capabilities TEXT NOT NULL,
            platforms TEXT NOT NULL,
            body TEXT NOT NULL,
            UNIQUE(symbol, kind)
        );

        CREATE INDEX idx_interfaces_symbol ON interfaces(symbol);
        CREATE INDEX idx_interfaces_short_name ON interfaces(short_name);
        CREATE INDEX idx_interfaces_component ON interfaces(component);
        CREATE INDEX idx_interfaces_kind ON interfaces(kind);
        CREATE INDEX idx_interfaces_visibility ON interfaces(visibility);

        CREATE VIRTUAL TABLE interface_fts USING fts5(
            interface_id UNINDEXED,
            symbol,
            short_name,
            component,
            summary,
            content,
            tokenize='trigram'
        );

        CREATE VIRTUAL TABLE document_fts USING fts5(
            docname UNINDEXED,
            title,
            content,
            tokenize='trigram'
        );
        """
    )


def _insert_documents(connection: sqlite3.Connection, documents: list[Document]) -> None:
    connection.executemany(
        """
        INSERT INTO documents(docname, title, source_url, local_path, crawled_at, content)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [
            (
                item.docname,
                item.title,
                item.source_url,
                item.local_path,
                item.crawled_at,
                item.content,
            )
            for item in documents
        ],
    )
    connection.executemany(
        "INSERT INTO document_fts(docname, title, content) VALUES (?, ?, ?)",
        [(item.docname, item.title, item.content) for item in documents],
    )


def _insert_interfaces(connection: sqlite3.Connection, interfaces: list[Interface]) -> None:
    for item in interfaces:
        cursor = connection.execute(
            """
            INSERT INTO interfaces(
                symbol, short_name, kind, component, module, class_name,
                signature, summary, parameters, returns_text, examples,
                source_url, source_anchor, docname, visibility,
                capabilities, platforms, body
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item.symbol,
                item.short_name,
                item.kind,
                item.component,
                item.module,
                item.class_name,
                item.signature,
                item.summary,
                item.parameters,
                item.returns,
                item.examples,
                item.source_url,
                item.source_anchor,
                item.docname,
                item.visibility,
                json.dumps(item.capabilities, ensure_ascii=False),
                json.dumps(item.platforms, ensure_ascii=False),
                item.body,
            ),
        )
        search_content = "\n".join(
            part
            for part in (
                item.signature,
                item.summary,
                item.parameters,
                item.returns,
                item.body,
                " ".join(item.capabilities),
                " ".join(item.platforms),
            )
            if part
        )
        connection.execute(
            """
            INSERT INTO interface_fts(
                interface_id, symbol, short_name, component, summary, content
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (cursor.lastrowid, item.symbol, item.short_name, item.component, item.summary, search_content),
        )


def build_index(snapshot_dir: Path, destination: Path) -> dict[str, Any]:
    """Build a complete SQLite index and atomically replace the old one."""

    snapshot_dir = snapshot_dir.resolve()
    destination = destination.resolve()
    manifest = _validate_snapshot(snapshot_dir)
    documents, interfaces = parse_snapshot(snapshot_dir)
    version, release_date = _latest_release(documents)

    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    os.close(descriptor)
    temporary_path = Path(temporary_name)

    try:
        connection = sqlite3.connect(temporary_path)
        try:
            _create_schema(connection)
            _insert_documents(connection, documents)
            _insert_interfaces(connection, interfaces)
            metadata = {
                "schema_version": SCHEMA_VERSION,
                "source_root": str(manifest.get("source_root", "")),
                "snapshot_generated_at": str(manifest.get("generated_at", "")),
                "ark_version": version,
                "ark_release_date": release_date,
                "document_count": str(len(documents)),
                "interface_count": str(len(interfaces)),
            }
            connection.executemany(
                "INSERT INTO metadata(key, value) VALUES (?, ?)", metadata.items()
            )
            connection.commit()
            result = connection.execute("PRAGMA integrity_check").fetchone()
            if not result or result[0] != "ok":
                raise RuntimeError(f"SQLite 索引完整性检查失败: {result}")
        finally:
            connection.close()
        os.replace(temporary_path, destination)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

    return {
        "database": str(destination),
        "documents": len(documents),
        "interfaces": len(interfaces),
        "ark_version": version,
        "release_date": release_date,
        "snapshot_generated_at": manifest.get("generated_at", ""),
    }


def _fts_terms(query: str) -> list[str]:
    terms: list[str] = []
    for token in re.findall(r"[A-Za-z0-9_.-]+|[\u3400-\u9fff]+", query.lower()):
        if re.search(r"[\u3400-\u9fff]", token) and len(token) > 4:
            terms.extend(token[index : index + 3] for index in range(len(token) - 2))
        elif len(token) >= 3:
            terms.append(token)
    return list(dict.fromkeys(terms))[:24]


def _fts_expression(query: str) -> str:
    return " OR ".join(f'"{term.replace(chr(34), chr(34) * 2)}"' for term in _fts_terms(query))


class ArkStore:
    """Read-only access to one immutable Orion Ark API index."""

    def __init__(self, database: Path):
        self.database = database.resolve()
        if not self.database.is_file():
            raise FileNotFoundError(
                f"Orion Ark 索引不存在: {self.database}; 请先运行 build-index"
            )

    def _connect(self) -> sqlite3.Connection:
        uri = f"file:{self.database.as_posix()}?mode=ro"
        connection = sqlite3.connect(uri, uri=True)
        connection.row_factory = sqlite3.Row
        return connection

    @staticmethod
    def _interface(row: sqlite3.Row, *, score: float | None = None) -> Interface:
        return Interface(
            symbol=row["symbol"],
            short_name=row["short_name"],
            kind=row["kind"],
            component=row["component"],
            module=row["module"],
            class_name=row["class_name"],
            signature=row["signature"],
            summary=row["summary"],
            parameters=row["parameters"],
            returns=row["returns_text"],
            examples=row["examples"],
            source_url=row["source_url"],
            source_anchor=row["source_anchor"],
            docname=row["docname"],
            visibility=row["visibility"],
            capabilities=json.loads(row["capabilities"]),
            platforms=json.loads(row["platforms"]),
            body=row["body"],
            score=score,
        )

    def metadata(self) -> dict[str, str]:
        with self._connect() as connection:
            rows = connection.execute("SELECT key, value FROM metadata ORDER BY key").fetchall()
        return {row["key"]: row["value"] for row in rows}

    def list_components(self) -> list[dict[str, Any]]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT component,
                       COUNT(*) AS interface_count,
                       COUNT(DISTINCT module) AS module_count,
                       SUM(CASE WHEN visibility = 'public' THEN 1 ELSE 0 END) AS public_count,
                       GROUP_CONCAT(DISTINCT kind) AS kinds
                FROM interfaces
                GROUP BY component
                ORDER BY component
                """
            ).fetchall()
        return [
            {
                "component": row["component"],
                "interface_count": row["interface_count"],
                "module_count": row["module_count"],
                "public_count": row["public_count"],
                "kinds": sorted((row["kinds"] or "").split(",")),
            }
            for row in rows
        ]

    @staticmethod
    def _filters(
        component: str | None,
        kind: str | None,
        visibility: str | None,
        *,
        alias: str = "i",
    ) -> tuple[str, list[str]]:
        conditions: list[str] = []
        values: list[str] = []
        for column, value in (
            ("component", component),
            ("kind", kind),
            ("visibility", visibility),
        ):
            if value:
                conditions.append(f"{alias}.{column} = ?")
                values.append(value)
        return (" AND ".join(conditions), values)

    def search_interfaces(
        self,
        query: str,
        *,
        component: str | None = None,
        kind: str | None = None,
        visibility: str | None = None,
        limit: int = 10,
    ) -> list[Interface]:
        query = query.strip()
        limit = max(1, min(limit, 50))
        filter_sql, filter_values = self._filters(component, kind, visibility)
        candidates: dict[int, tuple[sqlite3.Row, float]] = {}

        with self._connect() as connection:
            exact_conditions = []
            exact_values: list[Any] = []
            if query:
                exact_conditions.append(
                    "(LOWER(i.symbol) = LOWER(?) OR LOWER(i.short_name) = LOWER(?) "
                    "OR LOWER(i.symbol) LIKE LOWER(?))"
                )
                exact_values.extend([query, query, f"%{query}%"])
            if filter_sql:
                exact_conditions.append(filter_sql)
                exact_values.extend(filter_values)
            exact_where = " AND ".join(exact_conditions) or "1 = 1"
            exact_rows = connection.execute(
                f"SELECT i.* FROM interfaces i WHERE {exact_where} ORDER BY LENGTH(i.symbol), i.symbol LIMIT ?",
                [*exact_values, limit * 3],
            ).fetchall()
            for row in exact_rows:
                if query and row["short_name"].lower() == query.lower():
                    score = 100.0
                elif query and row["symbol"].lower() == query.lower():
                    score = 98.0
                elif query:
                    score = 82.0
                else:
                    score = 40.0
                candidates[row["id"]] = (row, score)

            expression = _fts_expression(query)
            if expression:
                fts_conditions = ["interface_fts MATCH ?"]
                fts_values: list[Any] = [expression]
                if filter_sql:
                    fts_conditions.append(filter_sql)
                    fts_values.extend(filter_values)
                try:
                    fts_rows = connection.execute(
                        f"""
                        SELECT i.*, bm25(interface_fts) AS text_rank
                        FROM interface_fts
                        JOIN interfaces i ON i.id = CAST(interface_fts.interface_id AS INTEGER)
                        WHERE {' AND '.join(fts_conditions)}
                        ORDER BY text_rank
                        LIMIT ?
                        """,
                        [*fts_values, limit * 5],
                    ).fetchall()
                except sqlite3.OperationalError:
                    fts_rows = []
                for position, row in enumerate(fts_rows):
                    score = 70.0 - min(position, 40) * 0.5
                    previous = candidates.get(row["id"])
                    if not previous or score > previous[1]:
                        candidates[row["id"]] = (row, score)

            if query and len(candidates) < limit:
                like_conditions = [
                    "(i.summary LIKE ? OR i.body LIKE ? OR i.parameters LIKE ? OR i.returns_text LIKE ?)"
                ]
                like_values: list[Any] = [f"%{query}%"] * 4
                if filter_sql:
                    like_conditions.append(filter_sql)
                    like_values.extend(filter_values)
                rows = connection.execute(
                    f"SELECT i.* FROM interfaces i WHERE {' AND '.join(like_conditions)} LIMIT ?",
                    [*like_values, limit * 3],
                ).fetchall()
                for position, row in enumerate(rows):
                    candidates.setdefault(row["id"], (row, 55.0 - position * 0.2))

        ranked = sorted(candidates.values(), key=lambda item: (-item[1], item[0]["symbol"]))
        return [self._interface(row, score=round(score, 2)) for row, score in ranked[:limit]]

    def get_interface(self, symbol: str) -> list[Interface]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT * FROM interfaces
                WHERE LOWER(symbol) = LOWER(?) OR LOWER(short_name) = LOWER(?)
                ORDER BY CASE WHEN LOWER(symbol) = LOWER(?) THEN 0 ELSE 1 END,
                         visibility DESC, symbol
                LIMIT 50
                """,
                (symbol, symbol, symbol),
            ).fetchall()
        return [self._interface(row) for row in rows]

    def get_document(self, docname: str) -> Document | None:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT * FROM documents WHERE docname = ?", (docname,)
            ).fetchone()
        if not row:
            return None
        return Document(
            docname=row["docname"],
            title=row["title"],
            source_url=row["source_url"],
            local_path=row["local_path"],
            crawled_at=row["crawled_at"],
            content=row["content"],
        )

    def list_documents(self) -> list[Document]:
        with self._connect() as connection:
            rows = connection.execute("SELECT * FROM documents ORDER BY docname").fetchall()
        return [
            Document(
                docname=row["docname"],
                title=row["title"],
                source_url=row["source_url"],
                local_path=row["local_path"],
                crawled_at=row["crawled_at"],
                content=row["content"],
            )
            for row in rows
        ]

    def search_documents(self, query: str, *, limit: int = 5) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 20))
        expression = _fts_expression(query)
        if not expression:
            return []
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT d.docname, d.title, d.source_url, d.content,
                       bm25(document_fts) AS text_rank
                FROM document_fts
                JOIN documents d ON d.docname = document_fts.docname
                WHERE document_fts MATCH ?
                ORDER BY text_rank
                LIMIT ?
                """,
                (expression, limit),
            ).fetchall()
        return [
            {
                "docname": row["docname"],
                "title": row["title"],
                "source_url": row["source_url"],
                "excerpt": _excerpt(row["content"], query),
            }
            for row in rows
        ]


def _excerpt(content: str, query: str, *, radius: int = 280) -> str:
    lowered = content.lower()
    positions = [
        lowered.find(term.lower())
        for term in _fts_terms(query)
        if lowered.find(term.lower()) >= 0
    ]
    position = min(positions) if positions else 0
    start = max(0, position - radius)
    end = min(len(content), position + radius)
    prefix = "…" if start else ""
    suffix = "…" if end < len(content) else ""
    return prefix + content[start:end].strip() + suffix
