"""Глобальные пути и неизменяемые константы FACE SHIFT.

Все игровые параметры (баланс, AI, тексты, карты) лежат в data/ и
редактируются без изменения кода. Здесь только то, что нужно для запуска.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "assets"
DATA_DIR = ROOT / "data"
SAVES_DIR = ROOT / "saves"
MODELS_DIR = ROOT / "models"
LOGS_DIR = ROOT / "logs"
SCREENSHOTS_DIR = ROOT / "screenshots"

GAME_TITLE = "FACE SHIFT: Ограбление века"
GAME_TITLE_EN = "FACE SHIFT: The Grand Heist"
VERSION = "1.0.0"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TILE_SIZE = 32

FACE_MODEL_PATH = MODELS_DIR / "face_landmarker.task"
ASSET_MANIFEST = ASSETS_DIR / "manifest.json"
# Увеличьте, если поменяли генератор ресурсов и хотите пересоздать PNG/WAV.
ASSET_VERSION = 4


def load_json(path: Path | str) -> Any:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path: Path | str, data: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def game_config(name: str) -> Any:
    """Читает data/game_config/<name>.json."""
    return load_json(DATA_DIR / "game_config" / f"{name}.json")
