from __future__ import annotations

from pathlib import Path

import pytest

from orion_ark_mcp.service import ArkKnowledgeService
from orion_ark_mcp.store import ArkStore, build_index


REPOSITORY_DIR = Path(__file__).resolve().parents[2]
SNAPSHOT_DIR = REPOSITORY_DIR / "result" / "orion" / "ark"


@pytest.fixture(scope="session")
def database(tmp_path_factory: pytest.TempPathFactory) -> Path:
    destination = tmp_path_factory.mktemp("orion-ark-index") / "ark.db"
    build_index(SNAPSHOT_DIR, destination)
    return destination


@pytest.fixture(scope="session")
def service(database: Path) -> ArkKnowledgeService:
    return ArkKnowledgeService(ArkStore(database))

