"""
components/assets.py

ARRAI Assets Manager
"""

from __future__ import annotations

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"

LOGO_DIR = ASSETS_DIR / "logo"

ICON_DIR = ASSETS_DIR / "icons"

IMAGE_DIR = ASSETS_DIR / "images"

ILLUSTRATION_DIR = ASSETS_DIR / "illustrations"


# ----------------------------------------------------------
# LOGO
# ----------------------------------------------------------

LOGO_SYMBOL = LOGO_DIR / "arrai_symbol.png"

LOGO_HORIZONTAL = LOGO_DIR / "arrai_horizontal.png"

LOGO_WHITE = LOGO_DIR / "arrai_white.png"

LOGO_DARK = LOGO_DIR / "arrai_dark.png"


# ----------------------------------------------------------
# DEFAULT IMAGES
# ----------------------------------------------------------

HERO_IMAGE = ILLUSTRATION_DIR / "hero.png"

EMPTY_STATE = IMAGE_DIR / "empty_state.png"

NOT_FOUND = IMAGE_DIR / "404.png"