"""Точка входа FACE SHIFT: Ограбление века.

Запуск:  python main.py            — игра
         python main.py --windowed — без полноэкранного режима из настроек
         python main.py --regen    — пересоздать сгенерированную графику и звук
"""
from __future__ import annotations

import sys

import config
from game.core.logger import setup_logging


def main(argv: list[str]) -> int:
    log = setup_logging()
    log.info("Запуск %s v%s, Python %s", config.GAME_TITLE, config.VERSION, sys.version.split()[0])

    from tools.generate_assets import ensure_assets
    ensure_assets(force="--regen" in argv)

    from game.core.app import App
    app = App(force_windowed="--windowed" in argv)
    try:
        app.run()
    except Exception:  # диагностика: полный стек в logs/face_shift.log
        log.exception("Необработанная ошибка в игровом цикле")
        return 1
    finally:
        app.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
