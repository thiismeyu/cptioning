"""
ARRAI

Application Entry Point
"""

from __future__ import annotations

import streamlit as st

from config import (
    APP_TITLE,
    DEFAULT_LAYOUT,
    DEFAULT_PAGE_ICON,
    DEFAULT_SIDEBAR,
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


# ==========================================================
# STREAMLIT CONFIG
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=DEFAULT_PAGE_ICON,
    layout=DEFAULT_LAYOUT,
    initial_sidebar_state=DEFAULT_SIDEBAR,
)


# ==========================================================
# GLOBAL FONT
# ==========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*{
    font-family:'Inter',sans-serif!important;
}

html{
    scroll-behavior:smooth;
}

</style>
""",
    unsafe_allow_html=True,
)


# ==========================================================
# LOAD STYLES
# ==========================================================

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


# ==========================================================
# SESSION
# ==========================================================

st.session_state.setdefault(
    "initialized",
    True,
)


# ==========================================================
# START APPLICATION
# ==========================================================

st.switch_page(
    "pages/1_Home.py",
)