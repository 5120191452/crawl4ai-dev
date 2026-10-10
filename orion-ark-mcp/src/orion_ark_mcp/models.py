"""Domain models shared by parsing, storage, recommendation, and MCP layers."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class Document:
    docname: str
    title: str
    source_url: str
    local_path: str
    crawled_at: str
    content: str

    def to_dict(self, *, include_content: bool = True) -> dict[str, Any]:
        result = asdict(self)
        if not include_content:
            result.pop("content", None)
        return result


@dataclass(slots=True)
class Interface:
    symbol: str
    short_name: str
    kind: str
    component: str
    module: str
    class_name: str | None
    signature: str
    summary: str
    parameters: str
    returns: str
    examples: str
    source_url: str
    source_anchor: str
    docname: str
    visibility: str
    capabilities: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    body: str = ""
    score: float | None = None

    def to_dict(self, *, include_body: bool = False) -> dict[str, Any]:
        result = asdict(self)
        if not include_body:
            result.pop("body", None)
        if self.score is None:
            result.pop("score", None)
        return result


@dataclass(slots=True)
class Scenario:
    id: str
    title: str
    description: str
    keywords: list[str]
    components: list[str]
    preferred_names: list[str]
    prerequisites: list[str]
    workflow: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

