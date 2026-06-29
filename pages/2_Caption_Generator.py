"""
pages/2_Caption_Generator.py
"""

from config import (
    CSS_VARIABLES,
    CSS_THEME,
    CSS_NAVIGATION,
    CSS_HERO,
    CSS_CARDS,
    CSS_CAPTION,
    CSS_ABOUT,
    CSS_FOOTER,
    CSS_ANIMATIONS,
    CSS_RESPONSIVE,
)

from utils.helpers import load_css_files

load_css_files(
    CSS_VARIABLES,
    CSS_THEME,
    CSS_NAVIGATION,
    CSS_HERO,
    CSS_CARDS,
    CSS_CAPTION,
    CSS_ABOUT,
    CSS_FOOTER,
    CSS_ANIMATIONS,
    CSS_RESPONSIVE,
)

from controllers.caption_controller import render_caption_page



render_caption_page()