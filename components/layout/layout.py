"""
components/layout/layout.py

ARRAI Layout
"""

from __future__ import annotations

from components.layout.navigation import render_navigation
from components.layout.footer import render_footer


def start_layout() -> None:
    """
    Render global navigation.
    """
    render_navigation()


def end_layout() -> None:
    """
    Render global footer.
    """
    render_footer()