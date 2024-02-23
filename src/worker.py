from __future__ import annotations

from typing import Any

from uvicorn.workers import UvicornWorker


class GrooluUvicornWorker(UvicornWorker):
    CONFIG_KWARGS: dict[str, Any] = {'loop': 'uvloop', 'http': 'httptools'}
