"""Command-line entry point for indexing, diagnostics, and serving."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .config import db_path, docs_dir
from .service import ArkKnowledgeService
from .store import ArkStore, build_index


def _print(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def _service(database: Path) -> ArkKnowledgeService:
    return ArkKnowledgeService(ArkStore(database))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="orion-ark-mcp",
        description="Orion Ark API knowledge index and read-only MCP server",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="SQLite 索引路径；默认读取 ORION_ARK_MCP_DB 或项目 data 目录",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build-index", help="从 Crawl4AI Markdown 快照构建索引")
    build.add_argument(
        "--docs",
        type=Path,
        default=None,
        help="包含 manifest.json 和 pages/ 的抓取目录",
    )

    subparsers.add_parser("status", help="显示索引状态")
    subparsers.add_parser("list-components", help="列出 Ark 组件")

    search = subparsers.add_parser("search", help="搜索 Ark 接口")
    search.add_argument("query")
    search.add_argument("--component")
    search.add_argument("--kind")
    search.add_argument("--visibility")
    search.add_argument("--limit", type=int, default=10)

    detail = subparsers.add_parser("get", help="获取接口详情")
    detail.add_argument("symbol")

    recommend = subparsers.add_parser("recommend", help="按任务推荐 Ark 接口")
    recommend.add_argument("goal")
    recommend.add_argument("--platform")
    recommend.add_argument("--device-type")
    recommend.add_argument("--ark-version")
    recommend.add_argument("--limit", type=int, default=12)

    examples = subparsers.add_parser("examples", help="查找示例及相关文档")
    examples.add_argument("query")
    examples.add_argument("--limit", type=int, default=5)

    serve = subparsers.add_parser("serve", help="启动 MCP 服务")
    serve.add_argument(
        "--transport",
        choices=("stdio", "streamable-http"),
        default="stdio",
    )
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=9000)
    serve.add_argument("--path", default="/mcp")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    database = db_path(args.db)

    if args.command == "build-index":
        _print(build_index(docs_dir(args.docs), database))
        return 0

    if args.command == "serve":
        from .server import configure_database, run

        configure_database(database)
        try:
            run(
                transport=args.transport,
                host=args.host,
                port=args.port,
                path=args.path,
            )
        except KeyboardInterrupt:
            # A long-running MCP server is normally stopped with Ctrl+C.
            # Treat that expected shutdown as a clean CLI exit.
            pass
        return 0

    service = _service(database)
    if args.command == "status":
        _print(service.status())
    elif args.command == "list-components":
        _print(service.list_components())
    elif args.command == "search":
        _print(
            service.search_interfaces(
                args.query,
                component=args.component,
                kind=args.kind,
                visibility=args.visibility,
                limit=args.limit,
            )
        )
    elif args.command == "get":
        _print(service.get_interface(args.symbol))
    elif args.command == "recommend":
        _print(
            service.recommend_interfaces(
                args.goal,
                platform=args.platform,
                device_type=args.device_type,
                ark_version=args.ark_version,
                limit=args.limit,
            )
        )
    elif args.command == "examples":
        _print(service.get_examples(args.query, limit=args.limit))
    else:  # pragma: no cover - argparse prevents this branch.
        raise AssertionError(args.command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
