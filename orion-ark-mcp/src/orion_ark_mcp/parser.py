"""Parse Crawl4AI-generated Sphinx Markdown into a stable API catalog."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable
from urllib.parse import quote

from .models import Document, Interface


FRONT_MATTER_RE = re.compile(r"\A---\s*\n(?P<meta>.*?)\n---\s*\n", re.DOTALL)
MODULE_HEADING_RE = re.compile(r"^##\s+(?P<module>ark(?:\.[\w]+)+)\s+module\s*$")
CLASS_RE = re.compile(r"^_class\s+_(?P<declaration>ark\.[^\n]+?)\s*$")
CALLABLE_RE = re.compile(
    r"^(?P<modifier>_(?:abstract|static|classmethod)\s+_)?"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*|ark(?:\.[A-Za-z_][A-Za-z0-9_]*)+)"
    r"(?P<signature>\(.*\))(?:\s*→\s*(?P<return_type>.+))?\s*$"
)
LINK_RE = re.compile(r"\[([^\[\]]+)\]\([^)]+\)")
LABEL_RE = re.compile(
    r"^(Brief|Parameters|Returns|Return|Raises|Example|Examples):\s*$",
    re.IGNORECASE,
)

CAPABILITY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "connect": ("connect", "disconnect", "连接", "断开"),
    "initialize": ("init", "initialize", "初始化"),
    "read": ("read", "读取", "读数据"),
    "write": ("write", "写入", "写数据"),
    "erase": ("erase", "discard", "trim", "擦除"),
    "file": ("file", "directory", "文件", "目录"),
    "buffer": ("buffer", "缓存", "缓冲"),
    "power": ("power", "voltage", "current", "relay", "电源", "电压", "电流", "继电器"),
    "camera": ("camera", "photo", "video", "相机", "拍照", "录像"),
    "mobile": ("mobile", "android", "adb", "手机", "移动设备", "安卓"),
    "ui": ("appium", "element", "click", "swipe", "界面", "点击", "滑动"),
    "logging": ("logging", "logger", "log", "日志"),
    "notify": ("notify", "notification", "webhook", "通知"),
    "upgrade": ("upgrade", "firmware", "升级", "固件"),
    "command": ("command", "cmd", "std_cmd", "vu_cmd", "命令"),
    "visual": ("visual", "image", "图像", "二维码", "画质"),
    "temperature": ("oven", "temperature", "chamber", "温箱", "温度"),
}

PLATFORM_KEYWORDS: dict[str, tuple[str, ...]] = {
    "android": ("android", "adb", "appium", "安卓"),
    "windows": ("windows", "win32"),
    "linux": ("linux",),
    "emmc": ("emmc",),
    "sd": (" sd ", "sdcard", "sd card"),
    "usb": ("usb",),
    "nvme": ("nvme",),
}

INTERNAL_PATH_MARKERS = (
    ".adapters.",
    ".services.",
    ".third_party.",
    ".fallback.",
)


def _parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text

    metadata: dict[str, str] = {}
    for line in match.group("meta").splitlines():
        key, separator, raw_value = line.partition(":")
        if not separator:
            continue
        raw_value = raw_value.strip()
        try:
            value = json.loads(raw_value)
        except json.JSONDecodeError:
            value = raw_value.strip('"\'')
        metadata[key.strip()] = str(value)
    return metadata, text[match.end() :]


def _clean_inline(value: str) -> str:
    value = LINK_RE.sub(r"\1", value)
    value = value.replace("`", "")
    value = value.replace("_* ", "*").replace("_** ", "**")
    value = re.sub(r"(?<=\()_", "", value)
    value = re.sub(r"(?<=, )_", "", value)
    value = re.sub(r"_(?=\s*(?:,|\)))", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def _component_for(symbol: str, docname: str) -> str:
    candidate = symbol if symbol.startswith("ark.") else docname
    parts = candidate.split(".")
    if len(parts) > 1 and parts[1].startswith("ark_"):
        return parts[1]
    return "ark"


def _visibility(symbol: str, short_name: str, module: str) -> str:
    lowered = f".{symbol.lower()}."
    if short_name.startswith("_") or any(marker in lowered for marker in INTERNAL_PATH_MARKERS):
        return "internal"
    if "_interface" in module.lower() or symbol.count(".") <= 3:
        return "public"
    return "documented"


def _tags(text: str, mapping: dict[str, tuple[str, ...]]) -> list[str]:
    lowered = f" {text.lower()} "
    return [
        tag
        for tag, keywords in mapping.items()
        if any(keyword.lower() in lowered for keyword in keywords)
    ]


def _section(lines: list[str], names: set[str]) -> str:
    start: int | None = None
    collected: list[str] = []
    for index, line in enumerate(lines):
        normalized = line.strip().rstrip(":").lower()
        if start is None:
            if normalized in names:
                start = index + 1
            elif normalized.startswith(":return") and "return" in names:
                inline = line.partition(":return:")[2].strip()
                if inline:
                    collected.append(inline)
                start = index + 1
            continue
        if LABEL_RE.match(line.strip()) or line.strip().startswith(":return:"):
            break
        collected.append(line)
    return "\n".join(collected).strip()


def _summary(lines: list[str]) -> str:
    brief = _section(lines, {"brief"})
    if brief:
        return " ".join(part.strip() for part in brief.splitlines() if part.strip())

    ignored_prefixes = ("Bases:", "Parameters:", "Returns:", ":return:")
    for line in lines:
        candidate = line.strip()
        if not candidate or candidate.startswith(ignored_prefixes):
            continue
        if candidate.startswith(("* ", "**", "_ =", ">")):
            continue
        if candidate.startswith("@brief:"):
            candidate = candidate.removeprefix("@brief:").strip()
            candidate = re.split(r"\s+@(?:param|return|raises?):", candidate, maxsplit=1)[0]
        return _clean_inline(candidate)
    return ""


def _source_anchor(symbol: str) -> str:
    return quote(symbol, safe="._-")


def _iter_declarations(lines: list[str]) -> Iterable[dict[str, object]]:
    current_module = ""
    current_class: str | None = None
    in_code = False

    for line_number, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        if stripped.startswith("## "):
            current_class = None
            module_match = MODULE_HEADING_RE.match(stripped)
            current_module = module_match.group("module") if module_match else ""
            continue

        class_match = CLASS_RE.match(stripped)
        if class_match:
            declaration = class_match.group("declaration")
            symbol = declaration.split("(", 1)[0].strip()
            current_class = symbol
            module = symbol.rpartition(".")[0]
            yield {
                "line": line_number,
                "symbol": symbol,
                "short_name": symbol.rsplit(".", 1)[-1],
                "kind": "class",
                "module": module,
                "class_name": None,
                "signature": _clean_inline(declaration),
            }
            continue

        callable_match = CALLABLE_RE.match(stripped)
        if not callable_match:
            continue

        name = callable_match.group("name")
        # Dotted examples such as ``logger.info(...)`` are prose, while
        # documented module-level functions use their full ``ark.*`` name.
        if "." in name and not name.startswith("ark."):
            continue

        if name.startswith("ark."):
            symbol = name
            module = name.rpartition(".")[0]
            class_name = None
            kind = "function"
        elif current_class:
            symbol = f"{current_class}.{name}"
            module = current_module or current_class.rpartition(".")[0]
            class_name = current_class
            modifier = (callable_match.group("modifier") or "").strip("_ ")
            kind = {
                "abstract": "abstract_method",
                "static": "static_method",
                "classmethod": "class_method",
            }.get(modifier, "method")
        elif current_module:
            symbol = f"{current_module}.{name}"
            module = current_module
            class_name = None
            kind = "function"
        else:
            continue

        signature = f"{name}{callable_match.group('signature')}"
        if callable_match.group("return_type"):
            signature += f" -> {callable_match.group('return_type')}"
        yield {
            "line": line_number,
            "symbol": symbol,
            "short_name": name.rsplit(".", 1)[-1],
            "kind": kind,
            "module": module,
            "class_name": class_name,
            "signature": _clean_inline(signature),
        }


def parse_markdown(path: Path, *, pages_dir: Path) -> tuple[Document, list[Interface]]:
    """Parse one generated Markdown page."""

    text = path.read_text(encoding="utf-8")
    metadata, body = _parse_front_matter(text)
    docname = metadata.get("docname") or path.stem
    title = metadata.get("title") or docname
    source_url = metadata.get("source", "")
    document = Document(
        docname=docname,
        title=title,
        source_url=source_url,
        local_path=path.relative_to(pages_dir.parent).as_posix(),
        crawled_at=metadata.get("crawled_at", ""),
        content=body.strip(),
    )

    lines = body.splitlines()
    declarations = list(_iter_declarations(lines))
    interfaces: list[Interface] = []

    for index, declaration in enumerate(declarations):
        start = int(declaration["line"]) + 1
        next_declaration = (
            int(declarations[index + 1]["line"]) if index + 1 < len(declarations) else len(lines)
        )
        next_heading = next(
            (
                line_number
                for line_number in range(start, next_declaration)
                if lines[line_number].startswith("## ")
            ),
            next_declaration,
        )
        section_lines = lines[start:next_heading]
        section_body = "\n".join(section_lines).strip()
        symbol = str(declaration["symbol"])
        short_name = str(declaration["short_name"])
        module = str(declaration["module"])
        searchable = " ".join(
            [symbol, short_name, str(declaration["signature"]), section_body, title]
        )
        kind = str(declaration["kind"])
        if kind == "class" and re.search(r"Bases:\s*`?Enum`?", section_body):
            kind = "enum"

        interfaces.append(
            Interface(
                symbol=symbol,
                short_name=short_name,
                kind=kind,
                component=_component_for(symbol, docname),
                module=module,
                class_name=(
                    str(declaration["class_name"])
                    if declaration["class_name"] is not None
                    else None
                ),
                signature=str(declaration["signature"]),
                summary=_summary(section_lines),
                parameters=_section(section_lines, {"parameters"}),
                returns=_section(section_lines, {"returns", "return"}),
                examples=_section(section_lines, {"example", "examples"}),
                source_url=source_url,
                source_anchor=_source_anchor(symbol),
                docname=docname,
                visibility=_visibility(symbol, short_name, module),
                capabilities=_tags(searchable, CAPABILITY_KEYWORDS),
                platforms=_tags(searchable, PLATFORM_KEYWORDS),
                body=section_body,
            )
        )

    return document, interfaces


def parse_snapshot(snapshot_dir: Path) -> tuple[list[Document], list[Interface]]:
    """Parse every Markdown page in a validated crawler snapshot."""

    pages_dir = snapshot_dir / "pages"
    if not pages_dir.is_dir():
        raise FileNotFoundError(f"Markdown 页面目录不存在: {pages_dir}")

    documents: list[Document] = []
    best_interfaces: dict[tuple[str, str], Interface] = {}
    for path in sorted(pages_dir.glob("*.md")):
        document, interfaces = parse_markdown(path, pages_dir=pages_dir)
        documents.append(document)
        for interface in interfaces:
            key = (interface.symbol, interface.kind)
            existing = best_interfaces.get(key)
            if existing is None or len(interface.body) > len(existing.body):
                best_interfaces[key] = interface

    return documents, sorted(best_interfaces.values(), key=lambda item: (item.symbol, item.kind))
