from __future__ import annotations

import asyncio
from pathlib import Path

import pytest


mcp_module = pytest.importorskip("mcp")


def test_mcp_lists_and_calls_read_only_tools(database: Path) -> None:
    from mcp import Client

    from orion_ark_mcp.server import configure_database, mcp

    async def exercise() -> None:
        configure_database(database)
        # Pin the protocol in-process so this verifies our surface rather than
        # the SDK's transport auto-discovery path.
        async with Client(
            mcp, mode="2026-07-28", read_timeout_seconds=5
        ) as client:
            listed = await client.list_tools()
            names = {tool.name for tool in listed.tools}
            assert {
                "ark_status",
                "list_ark_components",
                "search_ark_interfaces",
                "get_ark_interface",
                "recommend_ark_interfaces",
                "get_ark_examples",
            } <= names

            result = await client.call_tool(
                "search_ark_interfaces", {"query": "cmdq_send", "limit": 3}
            )
            assert result.is_error is False
            assert result.structured_content["count"] >= 1

    asyncio.run(exercise())


def test_mcp_concrete_resources(database: Path) -> None:
    from mcp import Client

    from orion_ark_mcp.server import configure_database, mcp

    async def exercise() -> None:
        configure_database(database)
        async with Client(
            mcp, mode="2026-07-28", read_timeout_seconds=5
        ) as client:
            resources = await client.list_resources()
            uris = {str(item.uri) for item in resources.resources}
            assert "ark://docs/Overview" in uris
            assert "ark://catalog/components" in uris

            result = await client.read_resource("ark://docs/Overview")
            assert "Platform Goals" in result.contents[0].text

    asyncio.run(exercise())
