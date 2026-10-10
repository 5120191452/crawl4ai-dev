"""Deep-crawl the complete Orion Ark Sphinx documentation.

The public ``/ark`` route is only an iframe wrapper.  The Sphinx documentation
itself is served from the site root, so this crawler starts at ``/index.html``
and uses Sphinx's search index as the authoritative list of documentation
pages.  Crawl4AI still performs the link discovery and page traversal; the
search index keeps auxiliary pages such as ``search.html`` and ``genindex.html``
out of the crawl and provides a reliable completeness check.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, unquote, urlparse
from urllib.request import ProxyHandler, Request, build_opener

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai.deep_crawling.filters import URLFilter


BASE_URL = "http://orion.longsys.com"
START_URL = f"{BASE_URL}/index.html"
SEARCH_INDEX_URL = f"{BASE_URL}/searchindex.js"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "result" / "orion" / "ark"

SEARCH_INDEX_PATTERN = re.compile(
    r"Search\.setIndex\((\{.*\})\);?\s*$",
    re.DOTALL,
)
HEADER_LINK_PATTERN = re.compile(r"\[¶\]\([^)]+\)")
ABSOLUTE_DOC_LINK_PATTERN = re.compile(
    r"https?://orion\.longsys\.com/([^\s)#?]+\.html)(#[^\s)]*)?"
)


def parse_search_index(source: str) -> list[str]:
    """Return the Sphinx docnames contained in ``searchindex.js``."""

    match = SEARCH_INDEX_PATTERN.search(source)
    if not match:
        raise ValueError("无法解析 Sphinx searchindex.js")

    payload = json.loads(match.group(1))
    docnames = payload.get("docnames")

    if not isinstance(docnames, list) or not all(
        isinstance(item, str) and item for item in docnames
    ):
        raise ValueError("searchindex.js 中缺少有效的 docnames")

    # Preserve the index order while protecting the crawl from duplicates.
    return list(dict.fromkeys(docnames))


def fetch_expected_docnames(timeout: int = 30) -> list[str]:
    """Download the Sphinx search index used for crawl filtering/validation."""

    request = Request(
        SEARCH_INDEX_URL,
        headers={"User-Agent": "Orion-Ark-Crawl4AI/1.0"},
    )
    # Internal Orion hosts must be reached directly.  Explicitly avoid
    # inheriting HTTP(S)_PROXY from the developer workstation.
    opener = build_opener(ProxyHandler({}))
    with opener.open(request, timeout=timeout) as response:
        source = response.read().decode("utf-8")
    return parse_search_index(source)


def url_to_docname(url: str) -> str | None:
    """Convert a Sphinx HTML URL into its search-index docname."""

    path = unquote(urlparse(url).path).lstrip("/")
    if not path.endswith(".html"):
        return None
    return path[: -len(".html")]


def docname_to_relative_path(docname: str) -> Path:
    """Map a trusted Sphinx docname to its local Markdown path."""

    pure_path = PurePosixPath(f"{docname}.md")
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise ValueError(f"不安全的 Sphinx docname: {docname!r}")
    return Path(*pure_path.parts)


def markdown_link(relative_path: Path) -> str:
    """Return a portable, URL-escaped Markdown destination."""

    return quote(relative_path.as_posix(), safe="/._-")


class SphinxDocumentFilter(URLFilter):
    """Allow only pages declared by the Sphinx search index."""

    __slots__ = ("_allowed_docnames",)

    def __init__(self, allowed_docnames: set[str]):
        super().__init__()
        self._allowed_docnames = frozenset(allowed_docnames)

    def apply(self, url: str) -> bool:
        passed = url_to_docname(url) in self._allowed_docnames
        self._update_stats(passed)
        return passed


def get_markdown(result: Any) -> str:
    """Support both string and MarkdownGenerationResult return values."""

    markdown = getattr(result, "markdown", None)
    if not markdown:
        return ""
    if isinstance(markdown, str):
        return markdown
    return getattr(markdown, "raw_markdown", None) or str(markdown)


def rewrite_document_links(markdown: str, expected_docnames: set[str]) -> str:
    """Rewrite absolute Ark HTML links to local Markdown files."""

    def replace(match: re.Match[str]) -> str:
        html_path = unquote(match.group(1))
        docname = html_path[: -len(".html")]
        if docname not in expected_docnames:
            return match.group(0)

        target = markdown_link(docname_to_relative_path(docname))
        return f"{target}{match.group(2) or ''}"

    return ABSOLUTE_DOC_LINK_PATTERN.sub(replace, markdown)


def clean_markdown(markdown: str, expected_docnames: set[str]) -> str:
    """Remove Sphinx chrome left in the article and localize doc links."""

    markdown = HEADER_LINK_PATTERN.sub("", markdown)
    markdown = rewrite_document_links(markdown, expected_docnames)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown)
    return markdown.strip()


def markdown_title(markdown: str, metadata: dict[str, Any]) -> str:
    """Prefer the article H1 and fall back to the HTML title/docname."""

    heading = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    if heading:
        return heading.group(1).strip()
    return str(metadata.get("title") or "Untitled").strip()


def page_document(
    *,
    title: str,
    docname: str,
    source_url: str,
    depth: int,
    crawled_at: str,
    markdown: str,
) -> str:
    """Add stable provenance metadata to one generated Markdown page."""

    front_matter = {
        "title": title,
        "docname": docname,
        "source": source_url,
        "depth": depth,
        "crawled_at": crawled_at,
    }
    yaml_lines = [
        f"{key}: {json.dumps(value, ensure_ascii=False)}"
        for key, value in front_matter.items()
    ]
    return "---\n" + "\n".join(yaml_lines) + f"\n---\n\n{markdown}\n"


def build_index(
    *,
    generated_at: str,
    expected_count: int,
    pages: list[dict[str, Any]],
    missing: list[str],
    failures: list[dict[str, str]],
) -> str:
    """Build a human-readable crawl index."""

    complete = not missing and not failures and len(pages) == expected_count
    lines = [
        "# Orion Ark 技术文档",
        "",
        f"> 文档入口：{START_URL}",
        f"> 生成时间：{generated_at}",
        "",
        "## 抓取结果",
        "",
        f"- Sphinx 索引页数：**{expected_count}**",
        f"- 成功生成：**{len(pages)}**",
        f"- 缺失页面：**{len(missing)}**",
        f"- 失败页面：**{len(failures)}**",
        f"- 完整性校验：**{'通过' if complete else '未通过'}**",
        "",
        "## 文档目录",
        "",
        "| 序号 | 文档 | Docname | 深度 | Markdown | 来源 |",
        "| ---: | --- | --- | ---: | --- | --- |",
    ]

    for index, page in enumerate(pages, 1):
        title = str(page["title"]).replace("|", "\\|")
        docname = str(page["docname"]).replace("|", "\\|")
        local_link = markdown_link(Path("pages") / Path(page["file"]))
        lines.append(
            f"| {index} | {title} | `{docname}` | {page['depth']} "
            f"| [打开]({local_link}) | [源页面]({page['url']}) |"
        )

    if missing:
        lines.extend(["", "## 缺失页面", ""])
        lines.extend(f"- `{docname}`" for docname in missing)

    if failures:
        lines.extend(["", "## 抓取失败", ""])
        lines.extend(
            f"- [{failure['url']}]({failure['url']})：{failure['error']}"
            for failure in failures
        )

    return "\n".join(lines) + "\n"


def prune_stale_pages(pages_dir: Path, expected_files: set[Path]) -> None:
    """Remove only stale Markdown files previously generated in ``pages``."""

    if not pages_dir.exists():
        return

    for candidate in pages_dir.rglob("*.md"):
        relative = candidate.relative_to(pages_dir)
        if relative not in expected_files:
            candidate.unlink()

    # Remove empty directories from deepest to shallowest.
    directories = sorted(
        (path for path in pages_dir.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for directory in directories:
        try:
            directory.rmdir()
        except OSError:
            pass


async def crawl_ark(
    *,
    output_dir: Path,
    headless: bool,
    verbose: bool,
    use_cache: bool,
) -> int:
    """Run the complete crawl and return a process-style exit code."""

    print(f"读取 Sphinx 索引：{SEARCH_INDEX_URL}")
    docnames = await asyncio.to_thread(fetch_expected_docnames)
    expected_docnames = set(docnames)
    expected_files = {
        docname_to_relative_path(docname) for docname in expected_docnames
    }

    print(f"索引包含 {len(docnames)} 个文档页")

    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    strategy = BFSDeepCrawlStrategy(
        max_depth=10,
        include_external=False,
        filter_chain=FilterChain(
            [
                DomainFilter(allowed_domains=["orion.longsys.com"]),
                SphinxDocumentFilter(expected_docnames),
            ]
        ),
    )

    browser_config = BrowserConfig(
        headless=headless,
        verbose=verbose,
    )
    run_config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        scraping_strategy=LXMLWebScrapingStrategy(),
        cache_mode=CacheMode.ENABLED if use_cache else CacheMode.BYPASS,
        stream=True,
        word_count_threshold=0,
        target_elements=["#furo-main-content"],
        excluded_selector=".headerlink, .back-to-top",
        remove_forms=True,
        wait_until="domcontentloaded",
        page_timeout=60_000,
        delay_before_return_html=0.0,
        semaphore_count=4,
        mean_delay=0.05,
        max_range=0.15,
        verbose=verbose,
    )

    generated_at = datetime.now(timezone.utc).isoformat()
    pages_by_docname: dict[str, dict[str, Any]] = {}
    failures: list[dict[str, str]] = []

    print(f"开始 Crawl4AI BFS 深度遍历：{START_URL}")
    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(url=START_URL, config=run_config)
        async for result in results:
            docname = url_to_docname(result.url)
            if docname not in expected_docnames:
                continue

            if not result.success:
                failures.append(
                    {
                        "url": result.url,
                        "error": result.error_message or "未知错误",
                    }
                )
                print(f"[失败] {docname}: {result.error_message}")
                continue

            markdown = clean_markdown(
                get_markdown(result),
                expected_docnames,
            )
            if not markdown:
                failures.append(
                    {
                        "url": result.url,
                        "error": "正文 Markdown 为空",
                    }
                )
                print(f"[失败] {docname}: 正文 Markdown 为空")
                continue

            metadata = result.metadata or {}
            depth = int(metadata.get("depth", 0) or 0)
            title = markdown_title(markdown, metadata)
            relative_path = docname_to_relative_path(docname)
            output_file = pages_dir / relative_path
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(
                page_document(
                    title=title,
                    docname=docname,
                    source_url=result.url,
                    depth=depth,
                    crawled_at=generated_at,
                    markdown=markdown,
                ),
                encoding="utf-8",
            )

            pages_by_docname[docname] = {
                "docname": docname,
                "title": title,
                "url": result.url,
                "file": relative_path.as_posix(),
                "depth": depth,
                "markdown_chars": len(markdown),
            }
            print(
                f"[{len(pages_by_docname):03d}/{len(docnames):03d}] "
                f"depth={depth} {docname}"
            )

    missing = sorted(expected_docnames - pages_by_docname.keys(), key=str.casefold)
    successful_files = {
        Path(page["file"]) for page in pages_by_docname.values()
    }
    prune_stale_pages(pages_dir, successful_files & expected_files)

    pages = sorted(
        pages_by_docname.values(),
        key=lambda page: docnames.index(page["docname"]),
    )
    complete = not missing and not failures and len(pages) == len(docnames)

    manifest = {
        "schema_version": 1,
        "source_root": START_URL,
        "search_index": SEARCH_INDEX_URL,
        "generated_at": generated_at,
        "expected_count": len(docnames),
        "success_count": len(pages),
        "missing_count": len(missing),
        "failure_count": len(failures),
        "complete": complete,
        "pages": pages,
        "missing": missing,
        "failures": failures,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "index.md").write_text(
        build_index(
            generated_at=generated_at,
            expected_count=len(docnames),
            pages=pages,
            missing=missing,
            failures=failures,
        ),
        encoding="utf-8",
    )

    print("=" * 72)
    print(f"预期：{len(docnames)}")
    print(f"成功：{len(pages)}")
    print(f"缺失：{len(missing)}")
    print(f"失败：{len(failures)}")
    print(f"完整性校验：{'通过' if complete else '未通过'}")
    print(f"输出目录：{output_dir.resolve()}")
    return 0 if complete else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="使用 Crawl4AI 深度遍历 Orion Ark 技术文档",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"输出目录（默认：{DEFAULT_OUTPUT_DIR}）",
    )
    parser.add_argument(
        "--headful",
        action="store_true",
        help="显示 Chromium 窗口，默认使用无头模式",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="显示 Crawl4AI 详细日志",
    )
    parser.add_argument(
        "--use-cache",
        action="store_true",
        help="允许使用 Crawl4AI 缓存，默认强制读取最新页面",
    )
    return parser.parse_args()


async def main() -> int:
    args = parse_args()
    return await crawl_ark(
        output_dir=args.output_dir.resolve(),
        headless=not args.headful,
        verbose=args.verbose,
        use_cache=args.use_cache,
    )


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
