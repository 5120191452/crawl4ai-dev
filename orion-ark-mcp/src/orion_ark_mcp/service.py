"""Application service used by both the CLI and MCP adapters."""

from __future__ import annotations

import json
import re
from importlib.resources import files
from typing import Any

from .models import Interface, Scenario
from .store import ArkStore


LIFECYCLE_NAMES = {
    "create_object",
    "open",
    "close",
    "init",
    "device_init",
    "connect",
    "disconnect",
    "power_connect",
    "power_disconnect",
}

INTENT_HINTS: tuple[tuple[re.Pattern[str], tuple[str, ...]], ...] = (
    (re.compile(r"erase|discard|trim|format|delete"), ("擦除", "格式化", "删除", "erase", "discard", "trim", "format", "delete")),
    (re.compile(r"record_video|video_start|video_stop"), ("录像", "录制", "视频", "record", "video")),
    (re.compile(r"take_photo|single_capture|continuous_capture"), ("拍照", "照片", "图片", "photo", "capture")),
    (re.compile(r"gallery_counts|get_file_num"), ("相册", "统计", "数量", "新增", "gallery", "count")),
    (re.compile(r"cmdq"), ("命令队列", "队列", "cmdq")),
    (re.compile(r"compare|check|verify"), ("比较", "校验", "验证", "检查", "compare", "check", "verify")),
    (re.compile(r"fill_data"), ("填充", "测试数据", "随机数据", "随机", "写入", "fill")),
    (re.compile(r"(^|_)read($|_)"), ("读取", "读写", "读数据", "read")),
    (re.compile(r"(^|_)write($|_)"), ("写入", "读写", "写数据", "write")),
    (re.compile(r"copy"), ("复制", "拷贝", "备份", "copy", "backup")),
    (re.compile(r"storage_info"), ("存储", "磁盘", "容量", "卷", "storage", "disk", "volume")),
    (re.compile(r"upgrade"), ("升级", "upgrade", "firmware")),
    (re.compile(r"power_down|power_off"), ("掉电", "断电", "下电", "power off", "power down")),
)


def load_scenarios() -> list[Scenario]:
    payload = json.loads(
        files("orion_ark_mcp").joinpath("scenarios.json").read_text(encoding="utf-8")
    )
    return [Scenario(**item) for item in payload]


def _interface_summary(item: Interface) -> dict[str, Any]:
    return {
        "symbol": item.symbol,
        "short_name": item.short_name,
        "kind": item.kind,
        "component": item.component,
        "signature": item.signature,
        "summary": item.summary,
        "visibility": item.visibility,
        "capabilities": item.capabilities,
        "platforms": item.platforms,
        "score": item.score,
        "source": f"{item.source_url}#{item.source_anchor}" if item.source_url else "",
    }


def _scenario_score(goal: str, scenario: Scenario) -> float:
    lowered = goal.lower()
    score = 0.0
    for keyword in scenario.keywords:
        keyword_lower = keyword.lower()
        if keyword_lower in lowered:
            score += 2.0 + min(len(keyword_lower), 8) / 8
    for component in scenario.components:
        if component.lower() in lowered:
            score += 4.0
    return score


def _intent_relevant(short_name: str, goal: str) -> bool:
    name = short_name.lower()
    if name in LIFECYCLE_NAMES:
        return True
    lowered_goal = goal.lower()
    if name in lowered_goal:
        return True
    for pattern, hints in INTENT_HINTS:
        if pattern.search(name):
            return any(hint in lowered_goal for hint in hints)
    return True


def _recommendation_alias_key(item: Interface) -> tuple[str, str]:
    # Sphinx often documents the same exported method under several module aliases.
    # A recommendation needs one callable family, while exact search keeps every alias.
    return item.component, item.short_name.lower()


def _phase(short_name: str) -> tuple[int, str]:
    name = short_name.lower()
    if re.search(r"create|factory|allocate|install", name):
        return 10, "创建组件或资源"
    if re.search(r"close|disconnect|clean|release|destroy|stop", name):
        return 90, "清理资源"
    if re.search(r"init|connect|open|config|configure|set_|enable|prepare", name):
        return 20, "初始化或配置"
    if re.search(r"get_|check|compare|verify|status|info|result|response", name):
        return 70, "读取或校验结果"
    return 50, "执行核心操作"


class ArkKnowledgeService:
    """High-level, read-only Orion Ark knowledge operations."""

    def __init__(self, store: ArkStore):
        self.store = store
        self.scenarios = load_scenarios()

    def status(self) -> dict[str, Any]:
        metadata = self.store.metadata()
        return {
            "status": "ready",
            "read_only": True,
            "database": str(self.store.database),
            **metadata,
        }

    def list_components(self) -> dict[str, Any]:
        metadata = self.store.metadata()
        return {
            "ark_version": metadata.get("ark_version", "unknown"),
            "snapshot_generated_at": metadata.get("snapshot_generated_at", ""),
            "components": self.store.list_components(),
        }

    def search_interfaces(
        self,
        query: str,
        *,
        component: str | None = None,
        kind: str | None = None,
        visibility: str | None = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        if not query.strip() and not component:
            raise ValueError("query 和 component 至少提供一个")
        items = self.store.search_interfaces(
            query,
            component=component,
            kind=kind,
            visibility=visibility,
            limit=limit,
        )
        metadata = self.store.metadata()
        return {
            "query": query,
            "filters": {
                "component": component,
                "kind": kind,
                "visibility": visibility,
            },
            "count": len(items),
            "items": [_interface_summary(item) for item in items],
            "ark_version": metadata.get("ark_version", "unknown"),
            "snapshot_generated_at": metadata.get("snapshot_generated_at", ""),
        }

    def get_interface(self, symbol: str) -> dict[str, Any]:
        matches = self.store.get_interface(symbol.strip())
        if not matches:
            suggestions = self.store.search_interfaces(symbol, limit=5)
            return {
                "found": False,
                "query": symbol,
                "suggestions": [_interface_summary(item) for item in suggestions],
            }
        return {
            "found": True,
            "query": symbol,
            "ambiguous": len(matches) > 1,
            "items": [
                {
                    **item.to_dict(include_body=True),
                    "source": (
                        f"{item.source_url}#{item.source_anchor}" if item.source_url else ""
                    ),
                }
                for item in matches
            ],
            "snapshot": self.store.metadata(),
        }

    def recommend_interfaces(
        self,
        goal: str,
        *,
        platform: str | None = None,
        device_type: str | None = None,
        ark_version: str | None = None,
        limit: int = 12,
    ) -> dict[str, Any]:
        goal = goal.strip()
        if not goal:
            raise ValueError("goal 不能为空")
        limit = max(1, min(limit, 30))
        metadata = self.store.metadata()

        ranked_scenarios = sorted(
            ((scenario, _scenario_score(goal, scenario)) for scenario in self.scenarios),
            key=lambda item: (-item[1], item[0].id),
        )
        matched_scenarios = [item for item in ranked_scenarios if item[1] > 0][:2]
        primary_components = set(matched_scenarios[0][0].components) if matched_scenarios else set()

        candidates: dict[tuple[str, str], tuple[Interface, float, Scenario | None]] = {}
        base_results = self.store.search_interfaces(goal, limit=50)
        for item in base_results:
            if matched_scenarios and (
                item.component not in primary_components or (item.score or 0.0) < 80.0
            ):
                continue
            candidates[(item.symbol, item.kind)] = (item, item.score or 0.0, None)

        for scenario, scenario_match_score in matched_scenarios:
            scenario_index = next(
                index
                for index, (candidate_scenario, _) in enumerate(matched_scenarios)
                if candidate_scenario.id == scenario.id
            )
            for component in scenario.components:
                if scenario_index > 0 and component not in primary_components:
                    continue
                component_results = self.store.search_interfaces(
                    goal, component=component, limit=25
                )
                for item in component_results:
                    if (item.score or 0.0) < 80.0:
                        continue
                    key = (item.symbol, item.kind)
                    score = (item.score or 0.0) + 18.0 + scenario_match_score
                    previous = candidates.get(key)
                    if not previous or score > previous[1]:
                        candidates[key] = (item, score, scenario)

            for preference_index, preferred_name in enumerate(scenario.preferred_names):
                if not _intent_relevant(preferred_name, goal):
                    continue
                # A secondary scenario contributes task actions but does not inject
                # another component lifecycle/factory into the recommended path.
                if scenario_index > 0 and preferred_name.lower() in LIFECYCLE_NAMES:
                    continue
                for component in scenario.components:
                    if scenario_index > 0 and component not in primary_components:
                        continue
                    preferred_results = self.store.search_interfaces(
                        preferred_name, component=component, limit=15
                    )
                    for item in preferred_results:
                        if item.short_name.lower() != preferred_name.lower():
                            continue
                        key = (item.symbol, item.kind)
                        score = 125.0 - preference_index + scenario_match_score
                        previous = candidates.get(key)
                        if not previous or score > previous[1]:
                            candidates[key] = (item, score, scenario)

        ranked: list[tuple[Interface, float, Scenario | None]] = []
        platform_lower = platform.lower() if platform else None
        for item, score, scenario in candidates.values():
            if not _intent_relevant(item.short_name, goal):
                continue
            if item.visibility == "internal":
                score -= 40.0
            elif item.visibility == "public":
                score += 10.0
            if item.kind in {"method", "abstract_method", "function"}:
                score += 4.0
            elif item.kind in {"class", "enum"}:
                score -= 3.0
            if platform_lower:
                if platform_lower in item.platforms or platform_lower in item.symbol.lower():
                    score += 10.0
                elif item.platforms:
                    score -= 4.0
            ranked.append((item, score, scenario))

        ranked.sort(key=lambda value: (-value[1], value[0].symbol))
        grouped: dict[tuple[str, str], tuple[Interface, float, Scenario | None]] = {}
        visibility_priority = {"public": 3, "documented": 2, "internal": 1}
        for candidate in ranked:
            alias_key = _recommendation_alias_key(candidate[0])
            previous = grouped.get(alias_key)
            if previous is None or (
                visibility_priority.get(candidate[0].visibility, 0), candidate[1]
            ) > (
                visibility_priority.get(previous[0].visibility, 0), previous[1]
            ):
                grouped[alias_key] = candidate
        deduplicated = sorted(grouped.values(), key=lambda value: (-value[1], value[0].symbol))
        selected = deduplicated[:limit]
        recommendations: list[dict[str, Any]] = []
        for item, score, scenario in selected:
            phase_order, role = _phase(item.short_name)
            preferred = bool(
                scenario
                and item.short_name.lower()
                in {name.lower() for name in scenario.preferred_names}
            )
            confidence = "high" if preferred else "medium" if scenario else "low"
            necessity = "required_candidate" if preferred else "supporting_candidate"
            reason = (
                f"匹配场景“{scenario.title}”，组件 {item.component}，用于{role}。"
                if scenario
                else f"与目标文本相关，组件 {item.component}，建议结合接口详情确认。"
            )
            recommendations.append(
                {
                    **_interface_summary(item),
                    "score": round(score, 2),
                    "necessity": necessity,
                    "role": role,
                    "call_order": phase_order,
                    "reason": reason,
                    "confidence": confidence,
                }
            )

        recommendations.sort(key=lambda item: (item["call_order"], -item["score"]))
        primary_scenario = matched_scenarios[0][0] if matched_scenarios else None
        missing_context: list[str] = []
        if primary_scenario and primary_scenario.id in {
            "device_io",
            "mobile_automation",
            "protocol_commands",
            "power_control",
        }:
            if not platform:
                missing_context.append("platform")
            if not device_type:
                missing_context.append("device_type")

        version_warning = None
        current_version = metadata.get("ark_version", "unknown")
        if ark_version and ark_version != current_version:
            version_warning = (
                f"请求版本为 {ark_version}，当前索引来自 {current_version}；"
                "返回结果不能保证与请求版本完全兼容。"
            )

        return {
            "goal": goal,
            "context": {
                "platform": platform,
                "device_type": device_type,
                "requested_ark_version": ark_version,
            },
            "matched_scenarios": [
                {**scenario.to_dict(), "match_score": round(score, 2)}
                for scenario, score in matched_scenarios
            ],
            "prerequisites": primary_scenario.prerequisites if primary_scenario else [],
            "suggested_workflow": primary_scenario.workflow if primary_scenario else [],
            "recommendations": recommendations,
            "missing_context": missing_context,
            "version_warning": version_warning,
            "ark_version": current_version,
            "snapshot_generated_at": metadata.get("snapshot_generated_at", ""),
            "notice": (
                "推荐结果是文档证据驱动的候选清单；执行破坏性设备操作前，"
                "必须核对具体接口参数、设备型号和版本。"
            ),
        }

    def get_examples(self, query: str, *, limit: int = 5) -> dict[str, Any]:
        interfaces = self.store.search_interfaces(query, limit=limit)
        interface_examples = [
            {
                "symbol": item.symbol,
                "example": item.examples,
                "source": f"{item.source_url}#{item.source_anchor}",
            }
            for item in interfaces
            if item.examples
        ]
        documents = self.store.search_documents(query, limit=limit)
        return {
            "query": query,
            "interface_examples": interface_examples,
            "document_matches": documents,
            "snapshot": self.store.metadata(),
        }

    def get_document(self, docname: str) -> dict[str, Any]:
        document = self.store.get_document(docname)
        if not document:
            raise KeyError(f"未找到文档: {docname}")
        return document.to_dict(include_content=True)
