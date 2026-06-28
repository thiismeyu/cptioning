"""
components/layout/layout.py

ARRAI Layout
"""

from __future__ import annotations

from components.layout.navigation import render_navigation
from components.layout.footer import render_footer


# ==========================================================
# START LAYOUT
# ==========================================================

def start_layout() -> None:
    render_navigation()


# ==========================================================
# END LAYOUT
# ==========================================================

def end_layout() -> None:
    render_footer()