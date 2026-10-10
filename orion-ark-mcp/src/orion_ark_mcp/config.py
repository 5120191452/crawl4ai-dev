"""Filesystem and runtime configuration."""

from __future__ import annotations

import os
from pathlib import Path


PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = PACKAGE_DIR.parent.parent
REPOSITORY_DIR = PROJECT_DIR.parent

DEFAULT_DOCS_DIR = REPOSITORY_DIR / "result" / "orion" / "ark"
DEFAULT_DB_PATH = PROJECT_DIR / "data" / "orion_ark.db"


def docs_dir(value: str | Path | None = None) -> Path:
    """Resolve the documentation snapshot directory."""

    configured = value or os.getenv("ORION_ARK_DOCS_DIR")
    return Path(configured).expanduser().resolve() if configured else DEFAULT_DOCS_DIR


def db_path(value: str | Path | None = None) -> Path:
    """Resolve the SQLite index location."""

    configured = value or os.getenv("ORION_ARK_MCP_DB")
    return Path(configured).expanduser().resolve() if configured else DEFAULT_DB_PATH

