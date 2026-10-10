import asyncio
import json
import math
import re
from pathlib import Path

from playwright.async_api import async_playwright


URL = "http://10.2.18.22:5000/tool_home"

OUTPUT_DIR = Path("result/orion/tool")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

JSON_FILE = OUTPUT_DIR / "artifacts.json"
MD_FILE = OUTPUT_DIR / "artifacts.md"

DEBUG_HTML = OUTPUT_DIR / "debug.html"
DEBUG_SCREENSHOT = OUTPUT_DIR / "debug.png"

PAGE_SIZE = 6


# ============================================================
# 文本处理
# ============================================================


def clean_text(text: str | None) -> str:
    if not text:
        return ""

    return re.sub(
        r"\s+",
        " ",
        text.strip(),
    )


# ============================================================
# 页面统计信息
# ============================================================


async def get_summary(page):
    body_text = await page.locator(
        "body"
    ).inner_text()

    def get_number(label: str) -> int:
        match = re.search(
            rf"{re.escape(label)}\s*(\d+)",
            body_text,
        )

        if match:
            return int(match.group(1))

        return 0

    return {
        "artifact_total":
            get_number("制品总数"),

        "version_total":
            get_number("版本总数"),

        "download_total":
            get_number("下载次数"),
    }


# ============================================================
# 当前页表格
# ============================================================


async def parse_current_page(page):
    rows = page.locator(
        "table tbody tr"
    )

    count = await rows.count()

    items = []

    for i in range(count):

        row = rows.nth(i)

        # 只处理可见行
        if not await row.is_visible():
            continue

        cells = row.locator("td")

        cell_count = await cells.count()

        if cell_count < 5:
            continue

        values = []

        for j in range(cell_count):

            value = await cells.nth(
                j
            ).inner_text()

            values.append(
                clean_text(value)
            )

        if not values[0]:
            continue

        items.append({
            "name":
                values[0],

            "version_count":
                values[1]
                if len(values) > 1
                else "",

            "latest_version":
                values[2]
                if len(values) > 2
                else "",

            "status":
                values[3]
                if len(values) > 3
                else "",

            "created_at":
                values[4]
                if len(values) > 4
                else "",
        })

    return items


# ============================================================
# 等待指定页真正加载完成
# ============================================================


async def wait_page_loaded(
    page,
    page_number: int,
    total: int,
):
    """
    第 2 页：
        显示 7-12 条，共 87 条

    第 15 页：
        显示 85-87 条，共 87 条
    """

    start = (
        (page_number - 1)
        * PAGE_SIZE
        + 1
    )

    end = min(
        page_number * PAGE_SIZE,
        total,
    )

    print(
        f"等待分页状态："
        f"显示 {start}-{end} 条，共 {total} 条"
    )

    try:

        await page.wait_for_function(
            """
            ([start, end, total]) => {

                const text =
                    document.body.innerText
                    .replace(/\\s+/g, " ");

                const pattern =
                    new RegExp(
                        `显示\\\\s*${start}\\\\s*-\\\\s*${end}`
                        + `\\\\s*条.*?共\\\\s*${total}\\\\s*条`
                    );

                return pattern.test(text);
            }
            """,
            [start, end, total],
            timeout=10000,
        )

        # 给 table DOM 再留一点更新时间
        await page.wait_for_timeout(
            300
        )

        return True

    except Exception:

        return False


# ============================================================
# 当前激活页
# ============================================================


async def get_active_page(page):
    """
    当前页按钮的 class 中包含：

        border-primary
        bg-primary
        text-white
    """

    buttons = page.locator(
        "button.pagination-btn"
    )

    count = await buttons.count()

    for i in range(count):

        button = buttons.nth(i)

        if not await button.is_visible():
            continue

        text = clean_text(
            await button.inner_text()
        )

        if not re.fullmatch(
            r"\d+",
            text,
        ):
            continue

        class_name = (
            await button.get_attribute(
                "class"
            )
            or ""
        )

        if (
            "bg-primary"
            in class_name
        ):
            return int(text)

    return None


# ============================================================
# 点击数字页码
# ============================================================


async def click_page_number(
    page,
    page_number: int,
):
    """
    使用页面真实 DOM：

        button.pagination-btn
    """

    target = str(page_number)

    buttons = page.locator(
        "button.pagination-btn"
    )

    count = await buttons.count()

    for i in range(count):

        button = buttons.nth(i)

        if not await button.is_visible():
            continue

        text = clean_text(
            await button.inner_text()
        )

        if text != target:
            continue

        print(
            f"找到页码按钮：{target}"
        )

        class_before = (
            await button.get_attribute(
                "class"
            )
        )

        print(
            "点击前 class：",
            class_before,
        )

        await button.click()

        return True

    return False


# ============================================================
# 点击下一页按钮
# ============================================================


async def click_next(page):
    """
    根据你真实页面 DOM：

    pagination-btn：

        [0] 空按钮 → 上一页
        [1..n]     → 数字
        [-1] 空按钮 → 下一页
    """

    buttons = page.locator(
        "button.pagination-btn"
    )

    count = await buttons.count()

    if count < 2:
        return False

    # 页面真实结构中最后一个 pagination-btn 是下一页
    next_button = buttons.nth(
        count - 1
    )

    if not await next_button.is_visible():
        return False

    class_name = (
        await next_button.get_attribute(
            "class"
        )
        or ""
    )

    print(
        "下一页按钮 class：",
        class_name,
    )

    # disabled 状态在你页面中表现为：
    #
    # opacity-50
    # cursor-not-allowed

    if (
        "cursor-not-allowed"
        in class_name
        or
        "opacity-50"
        in class_name
    ):
        print(
            "下一页按钮已经禁用"
        )

        return False

    print(
        "点击下一页箭头"
    )

    await next_button.click()

    return True


# ============================================================
# 分页按钮诊断
# ============================================================


async def print_pagination(page):

    buttons = page.locator(
        "button.pagination-btn"
    )

    count = await buttons.count()

    print()
    print(
        f"当前 pagination-btn 数量："
        f"{count}"
    )

    for i in range(count):

        button = buttons.nth(i)

        if not await button.is_visible():
            continue

        text = clean_text(
            await button.inner_text()
        )

        cls = (
            await button.get_attribute(
                "class"
            )
            or ""
        )

        print(
            f"[{i}] "
            f"text={text!r} "
            f"class={cls}"
        )


# ============================================================
# Debug
# ============================================================


async def save_debug(page):

    try:

        DEBUG_HTML.write_text(
            await page.content(),
            encoding="utf-8",
        )

        print(
            "Debug HTML：",
            DEBUG_HTML.resolve(),
        )

    except Exception as exc:

        print(
            "HTML保存失败：",
            exc,
        )

    try:

        await page.screenshot(
            path=str(
                DEBUG_SCREENSHOT
            ),
            full_page=True,
        )

        print(
            "Debug截图：",
            DEBUG_SCREENSHOT.resolve(),
        )

    except Exception as exc:

        print(
            "截图失败：",
            exc,
        )


# ============================================================
# Markdown
# ============================================================


def create_markdown(
    summary,
    items,
):

    lines = [
        "# Orion 制品管理系统",
        "",
        "> Orion 入口："
        "http://orion.longsys.com/tool",
        "",
        f"> 实际页面：{URL}",
        "",
        "## 数据概览",
        "",
        (
            "- 制品总数："
            f"**{summary['artifact_total']}**"
        ),
        (
            "- 版本总数："
            f"**{summary['version_total']}**"
        ),
        (
            "- 下载次数："
            f"**{summary['download_total']}**"
        ),
        "",
        "## 制品列表",
        "",
        (
            "| 序号 | 制品名称 | "
            "版本数 | 最新版本 | "
            "状态 | 创建时间 |"
        ),
        (
            "| ---: | --- | ---: | "
            "--- | --- | --- |"
        ),
    ]

    for i, item in enumerate(
        items,
        1,
    ):

        lines.append(
            f"| {i} "
            f"| {item['name']} "
            f"| {item['version_count']} "
            f"| {item['latest_version']} "
            f"| {item['status']} "
            f"| {item['created_at']} |"
        )

    return "\n".join(lines)


# ============================================================
# 主程序
# ============================================================


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False
        )

        context = await browser.new_context()

        page = await context.new_page()

        try:

            print("=" * 80)
            print("打开制品系统")
            print(URL)

            await page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            # =================================================
            # 等待第一页
            # =================================================

            await page.locator(
                "table tbody tr"
            ).first.wait_for(
                timeout=30000
            )

            await page.wait_for_timeout(
                1000
            )

            # =================================================
            # 概览
            # =================================================

            summary = await get_summary(
                page
            )

            total = summary[
                "artifact_total"
            ]

            expected_pages = math.ceil(
                total / PAGE_SIZE
            )

            print()
            print(
                "制品总数：",
                total,
            )

            print(
                "版本总数：",
                summary[
                    "version_total"
                ],
            )

            print(
                "下载次数：",
                summary[
                    "download_total"
                ],
            )

            print(
                "预计分页：",
                expected_pages,
            )

            await print_pagination(
                page
            )

            # =================================================
            # 开始抓
            # =================================================

            all_items = []

            seen_names = set()

            for target_page in range(
                1,
                expected_pages + 1,
            ):

                print()
                print("=" * 80)

                print(
                    f"目标页："
                    f"{target_page}"
                    f"/{expected_pages}"
                )

                # ---------------------------------------------
                # 第1页已经在当前页面
                # ---------------------------------------------

                if target_page > 1:

                    current_active = (
                        await get_active_page(
                            page
                        )
                    )

                    print(
                        "当前激活页：",
                        current_active,
                    )

                    # -----------------------------------------
                    # 先尝试直接点击数字
                    # -----------------------------------------

                    clicked = (
                        await click_page_number(
                            page,
                            target_page,
                        )
                    )

                    # -----------------------------------------
                    # 如果目标数字当前不可见
                    # 就使用右箭头
                    # -----------------------------------------

                    if not clicked:

                        print(
                            f"页码 "
                            f"{target_page} "
                            "当前不可见"
                        )

                        clicked = (
                            await click_next(
                                page
                            )
                        )

                    if not clicked:

                        print(
                            "❌ 无法翻页"
                        )

                        await print_pagination(
                            page
                        )

                        await save_debug(
                            page
                        )

                        break

                    # -----------------------------------------
                    # 等分页统计真正改变
                    # -----------------------------------------

                    loaded = (
                        await wait_page_loaded(
                            page,
                            target_page,
                            total,
                        )
                    )

                    if not loaded:

                        print(
                            "❌ 点击成功，"
                            "但分页统计没有变化"
                        )

                        print(
                            "当前激活页：",
                            await get_active_page(
                                page
                            )
                        )

                        await print_pagination(
                            page
                        )

                        await save_debug(
                            page
                        )

                        break

                    print(
                        "✅ 页面加载完成"
                    )

                # ---------------------------------------------
                # 当前页数据
                # ---------------------------------------------

                items = (
                    await parse_current_page(
                        page
                    )
                )

                print(
                    "当前页数据：",
                    len(items),
                    "条",
                )

                for item in items:

                    if (
                        item["name"]
                        in seen_names
                    ):
                        print(
                            "重复，跳过：",
                            item["name"],
                        )
                        continue

                    seen_names.add(
                        item["name"]
                    )

                    all_items.append(
                        item
                    )

                    print(
                        f"  "
                        f"{len(all_items):03d}. "
                        f"{item['name']} "
                        f"| "
                        f"{item['latest_version']} "
                        f"| "
                        f"{item['status']}"
                    )

                # ---------------------------------------------
                # 当前分页状态
                # ---------------------------------------------

                active = await get_active_page(
                    page
                )

                print(
                    "当前激活页：",
                    active,
                )

            # =================================================
            # 结果
            # =================================================

            print()
            print("=" * 80)
            print("抓取完成")
            print("=" * 80)

            print(
                "页面声明制品总数：",
                total,
            )

            print(
                "实际抓取制品总数：",
                len(all_items),
            )

            if len(all_items) == total:

                print(
                    "✅ 数量校验通过"
                )

            else:

                print(
                    "⚠️ 数量校验失败"
                )

            # =================================================
            # JSON
            # =================================================

            result = {
                "source": URL,
                "summary": summary,
                "actual_count":
                    len(all_items),
                "artifacts":
                    all_items,
            }

            JSON_FILE.write_text(
                json.dumps(
                    result,
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )

            # =================================================
            # Markdown
            # =================================================

            MD_FILE.write_text(
                create_markdown(
                    summary,
                    all_items,
                ),
                encoding="utf-8",
            )

            print()
            print(
                "JSON：",
                JSON_FILE.resolve(),
            )

            print(
                "Markdown：",
                MD_FILE.resolve(),
            )

        finally:

            await page.wait_for_timeout(
                3000
            )

            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())