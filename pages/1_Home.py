"""
pages/1_Home.py
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

from controllers.home_controller import render_home_page

render_home_page()