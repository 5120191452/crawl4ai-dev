from __future__ import annotations

from pathlib import Path

from orion_ark_mcp.parser import parse_markdown


def test_parse_sphinx_class_methods_and_return_type(tmp_path: Path) -> None:
    pages = tmp_path / "pages"
    pages.mkdir()
    document = pages / "ark.demo.md"
    document.write_text(
        """---
title: "Demo"
docname: "ark.demo"
source: "http://orion.example/ark.demo.html"
crawled_at: "2026-01-01T00:00:00Z"
---

# Demo
## ark.demo.interface module

_class _ark.demo.interface.DemoInterface

Bases: `ABC`

_abstract _read(_address : int_) → Tuple[int, bytes]

Brief:

Read bytes from the device.

Parameters:

**address** – Address to read.

Returns:

Status and data.

_static _validate(_value : int_) → bool

Validate a value.
""",
        encoding="utf-8",
    )

    parsed_document, interfaces = parse_markdown(document, pages_dir=pages)
    by_name = {item.short_name: item for item in interfaces}

    assert parsed_document.docname == "ark.demo"
    assert by_name["DemoInterface"].kind == "class"
    assert by_name["read"].kind == "abstract_method"
    assert by_name["read"].summary == "Read bytes from the device."
    assert "Tuple[int, bytes]" in by_name["read"].signature
    assert by_name["validate"].kind == "static_method"

