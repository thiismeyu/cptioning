"""
components/caption/export_panel.py

ARRAI Export Panel
"""

from __future__ import annotations

import json

import streamlit as st


def render_export_panel(
    english_caption: str,
    translated_caption: str,
    language_name: str,
):

    st.markdown(
        '<h2 class="section-title">Export Result</h2>',
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:

        st.download_button(

            "📄 Download TXT",

            translated_caption,

            file_name="caption.txt",

            use_container_width=True,

        )

    with c2:

        payload = {

            "english": english_caption,

            "translation": translated_caption,

            "language": language_name,

        }

        st.download_button(

            "🗂 Download JSON",

            json.dumps(payload, indent=4),

            file_name="caption.json",

            mime="application/json",

            use_container_width=True,

        )