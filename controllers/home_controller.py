"""
controllers/home_controller.py

ARRAI Home Controller
"""

from __future__ import annotations

import streamlit as st

from components.layout.layout import (
    start_layout,
    end_layout,
)

from components.sections.hero import render_hero
from components.sections.features import render_features
from components.sections.pipeline import render_pipeline
from components.sections.technology import render_technology
from components.sections.about import render_about
from components.sections.cta import render_cta


def render_home_page() -> None:
    """
    Render Home Page.
    """

    start_layout()

    # ======================================================
    # HERO
    # ======================================================

    render_hero()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    # ======================================================
    # FEATURES
    # ======================================================

    render_features()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    # ======================================================
    # PIPELINE
    # ======================================================

    render_pipeline()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    # ======================================================
    # TECHNOLOGY
    # ======================================================

    render_technology()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    # ======================================================
    # ABOUT
    # ======================================================

    render_about()

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    # ======================================================
    # CTA
    # ======================================================

    render_cta()

    end_layout()