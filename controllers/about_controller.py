"""
controllers/about_controller.py
"""

from __future__ import annotations

from components.layout.layout import (
    start_layout,
    end_layout,
)

from components.about.overview import render_overview
from components.about.information import render_information
from components.about.roadmap import render_roadmap


def render_about_page() -> None:

    start_layout()

    render_overview()

    render_information()

    render_roadmap()

    end_layout()