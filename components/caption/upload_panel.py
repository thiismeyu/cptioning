"""
components/caption/upload_panel.py
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


def render_upload_panel():

    section_title(
        "Upload Image",
        "PNG, JPG or JPEG image.",
    )

    return st.file_uploader(
        "",
        type=["png", "jpg", "jpeg"],
        label_visibility="collapsed",
        key="upload_image",
    )