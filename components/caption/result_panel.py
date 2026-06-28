"""
components/caption/result_panel.py

ARRAI Premium Result Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


# ==========================================================
# PRIVATE
# ==========================================================

def _caption_card(
    title: str,
    badge: str,
    caption: str,
) -> None:

    st.container(border=True)

    st.markdown(f"### {badge} {title}")

    st.write(caption)

# ==========================================================
# PUBLIC
# ==========================================================

def render_result_panel(
    english_caption: str,
    translated_caption: str,
    language_name: str,
    language_flag: str,
):

    st.success("RESULT PANEL TEST")

    st.write(english_caption)

    st.write(translated_caption)