"""
components/caption/workspace.py

ARRAI Caption Workspace
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from components.ui.section import section_title

from components.caption.upload_panel import render_upload_panel
from components.caption.preview_panel import render_preview_panel
from components.caption.language_panel import render_language_panel
from components.caption.generate_panel import render_generate_panel


# ==========================================================
# PUBLIC
# ==========================================================

def render_workspace() -> tuple[Any, str, str, bool]:
    """
    Render Caption Workspace.

    Returns
    -------
    uploaded_file
    language_name
    language_code
    generate_clicked
    """

    section_title(
        "Caption Workspace",
        "Upload an image and configure multilingual caption generation.",
    )

    left, right = st.columns(
        [1.35, .65],
        gap="large",
    )

    uploaded = None
    language_name = "English"
    language_code = "en"
    generate = False

    with left:

        uploaded = render_upload_panel()

        if uploaded is not None:

            render_preview_panel(uploaded)

    with right:

        language_name, language_code = render_language_panel()

        st.markdown("<br>", unsafe_allow_html=True)

        generate = render_generate_panel()

    return (
        uploaded,
        language_name,
        language_code,
        generate,
    )