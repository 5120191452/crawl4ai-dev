from __future__ import annotations

from orion_ark_mcp.service import ArkKnowledgeService


def _names(result: dict) -> list[str]:
    return [item["short_name"] for item in result["recommendations"]]


def test_device_read_write_recommendation_is_safe_and_ordered(
    service: ArkKnowledgeService,
) -> None:
    result = service.recommend_interfaces(
        "对存储设备进行随机读写并校验数据",
        platform="emmc",
        device_type="storage",
    )
    names = _names(result)

    assert result["matched_scenarios"][0]["id"] == "device_io"
    assert {"open", "device_init", "read", "write", "compare", "close"} <= set(names)
    assert "erase" not in names
    assert [item["call_order"] for item in result["recommendations"]] == sorted(
        item["call_order"] for item in result["recommendations"]
    )


def test_android_photo_recommendation_uses_public_mobile_api(
    service: ArkKnowledgeService,
) -> None:
    result = service.recommend_interfaces(
        "Android手机拍照后统计新增图片",
        platform="android",
        device_type="phone",
    )

    assert _names(result) == [
        "create_object",
        "connect",
        "take_photo",
        "get_gallery_counts",
        "disconnect",
    ]
    assert all(item["component"] == "ark_mobile" for item in result["recommendations"])
    assert all(item["visibility"] != "internal" for item in result["recommendations"])


def test_version_mismatch_is_explicit(service: ArkKnowledgeService) -> None:
    result = service.recommend_interfaces("设备读写", ark_version="2.4.0")

    assert result["version_warning"]
    assert "2.4.0" in result["version_warning"]
    assert "3.2.1" in result["version_warning"]

