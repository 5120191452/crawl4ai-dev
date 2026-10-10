from __future__ import annotations

from orion_ark_mcp.service import ArkKnowledgeService


def test_complete_snapshot_is_indexed(service: ArkKnowledgeService) -> None:
    status = service.status()

    assert status["status"] == "ready"
    assert status["document_count"] == "103"
    assert int(status["interface_count"]) >= 1800
    assert status["ark_version"] == "3.2.1"


def test_exact_interface_search_has_signature_and_source(
    service: ArkKnowledgeService,
) -> None:
    result = service.search_interfaces("cmdq_send", limit=5)

    assert result["items"]
    first = result["items"][0]
    assert first["short_name"] == "cmdq_send"
    assert first["component"] == "ark_device"
    assert "address" in first["signature"]
    assert first["source"].startswith("http://orion.longsys.com/")


def test_interface_detail_returns_parameters_and_provenance(
    service: ArkKnowledgeService,
) -> None:
    symbol = "ark.ark_device.device.ark_device_interface.ArkDeviceInterface.cmdq_send"
    result = service.get_interface(symbol)

    assert result["found"] is True
    assert result["ambiguous"] is False
    assert "queue_depth" not in result["items"][0]["parameters"]
    assert "address" in result["items"][0]["parameters"]
    assert result["items"][0]["docname"] == "ark.ark_device.device"


def test_unknown_interface_returns_search_suggestions(
    service: ArkKnowledgeService,
) -> None:
    result = service.get_interface("cmdq_sen")

    assert result["found"] is False
    assert any(item["short_name"] == "cmdq_send" for item in result["suggestions"])

