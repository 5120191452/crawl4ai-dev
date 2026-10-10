"""MCP protocol adapter for the Orion Ark knowledge service."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from mcp.server import MCPServer
from mcp.server.mcpserver.resources import TextResource
from mcp.types import ToolAnnotations

from .config import db_path
from .service import ArkKnowledgeService
from .store import ArkStore


mcp = MCPServer("Orion Ark API Guide")
READ_ONLY = ToolAnnotations(read_only_hint=True, open_world_hint=False)
_database_override: Path | None = None
_resources_registered_for: Path | None = None


def configure_database(database: str | Path | None) -> None:
    """Set the database before serving and clear the cached service."""

    global _database_override
    _database_override = Path(database).expanduser().resolve() if database else None
    _service.cache_clear()
    _register_resources()


@lru_cache(maxsize=1)
def _service() -> ArkKnowledgeService:
    return ArkKnowledgeService(ArkStore(db_path(_database_override)))


def _register_resources() -> None:
    """Register concrete text resources without function/thread wrappers."""

    global _resources_registered_for
    active_database = db_path(_database_override)
    if _resources_registered_for == active_database:
        return
    if _resources_registered_for is not None:
        raise RuntimeError("MCP server 实例已绑定其他数据库，请启动新进程切换索引")

    service = _service()
    for document in service.store.list_documents():
        content = (
            f"---\ntitle: {document.title!r}\nsource: {document.source_url!r}\n"
            f"crawled_at: {document.crawled_at!r}\n---\n\n{document.content}\n"
        )
        mcp.add_resource(
            TextResource(
                uri=f"ark://docs/{document.docname}",
                name=document.docname,
                title=document.title,
                description=f"Orion Ark 文档：{document.title}",
                mime_type="text/markdown",
                text=content,
            )
        )

    mcp.add_resource(
        TextResource(
            uri="ark://catalog/components",
            name="ark-components",
            title="Orion Ark 组件目录",
            description="Ark 组件及接口数量目录",
            mime_type="application/json",
            text=json.dumps(service.list_components(), ensure_ascii=False, indent=2),
        )
    )
    _resources_registered_for = active_database


@mcp.tool(title="Orion Ark 索引状态", annotations=READ_ONLY)
def ark_status() -> dict[str, Any]:
    """返回 Ark 文档版本、快照时间、文档数和接口数。"""

    return _service().status()


@mcp.tool(title="列出 Orion Ark 组件", annotations=READ_ONLY)
def list_ark_components() -> dict[str, Any]:
    """列出 Ark 组件、模块数、接口数和接口类型。"""

    return _service().list_components()


@mcp.tool(title="搜索 Orion Ark 接口", annotations=READ_ONLY)
def search_ark_interfaces(
    query: str,
    component: str | None = None,
    kind: str | None = None,
    visibility: str | None = None,
    limit: int = 10,
) -> dict[str, Any]:
    """按接口名、自然语言功能、组件或接口类型搜索 Ark API。

    Args:
        query: 接口名、功能或问题，例如 ``cmdq_send``、``设备读写``。
        component: 可选组件名，例如 ``ark_device``。
        kind: 可选类型：class、enum、method、abstract_method、static_method、
            class_method 或 function。
        visibility: 可选可见性：public、documented 或 internal。
        limit: 返回数量，范围 1 到 50。
    """

    return _service().search_interfaces(
        query,
        component=component,
        kind=kind,
        visibility=visibility,
        limit=limit,
    )


@mcp.tool(title="获取 Orion Ark 接口详情", annotations=READ_ONLY)
def get_ark_interface(symbol: str) -> dict[str, Any]:
    """获取接口签名、参数、返回值、正文、来源和版本信息。"""

    return _service().get_interface(symbol)


@mcp.tool(title="推荐 Orion Ark 接口", annotations=READ_ONLY)
def recommend_ark_interfaces(
    goal: str,
    platform: str | None = None,
    device_type: str | None = None,
    ark_version: str | None = None,
    limit: int = 12,
) -> dict[str, Any]:
    """根据任务目标推荐 Ark 接口候选、前置条件和调用阶段。

    结果严格来自当前文档索引。推荐是候选方案，不会调用真实设备，也不会执行
    擦除、写入、上下电等操作。

    Args:
        goal: 用户要完成的任务。
        platform: 可选平台或协议，例如 android、emmc、sd、usb。
        device_type: 可选设备型号或设备类型。
        ark_version: 用户项目使用的 Ark 版本，用于提示版本差异。
        limit: 最多返回的接口候选数，范围 1 到 30。
    """

    return _service().recommend_interfaces(
        goal,
        platform=platform,
        device_type=device_type,
        ark_version=ark_version,
        limit=limit,
    )


@mcp.tool(title="查找 Orion Ark 示例", annotations=READ_ONLY)
def get_ark_examples(query: str, limit: int = 5) -> dict[str, Any]:
    """按接口或场景查找接口示例和相关文档片段。"""

    return _service().get_examples(query, limit=limit)


def run(
    *,
    transport: str = "stdio",
    host: str = "127.0.0.1",
    port: int = 9000,
    path: str = "/mcp",
) -> None:
    """Run with a supported MCP transport."""

    _register_resources()
    if transport == "stdio":
        mcp.run(transport="stdio")
        return
    if transport == "streamable-http":
        mcp.run(
            transport="streamable-http",
            host=host,
            port=port,
            streamable_http_path=path,
            stateless_http=True,
            json_response=True,
        )
        return
    raise ValueError(f"不支持的 MCP transport: {transport}")
