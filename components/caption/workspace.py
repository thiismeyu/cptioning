"""
components/caption/workspace.py

ARRAI Caption Studio Workspace
Layout: LEFT (upload + preview + image info) | RIGHT (language + generate + empty state)
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from components.caption.upload_panel import render_upload_panel
from components.caption.preview_panel import render_preview_panel
from components.caption.language_panel import render_language_panel
from components.caption.generate_panel import render_generate_panel


# ==========================================================
# PRIVATE
# ==========================================================

def _render_page_header() -> None:

    st.markdown(
        """
<div class="studio-header">

  <div class="studio-header-left">

    <div class="studio-eyebrow">
      <span class="studio-dot"></span>
      CAPTION STUDIO
    </div>

    <h1 class="studio-title">
      Generate Caption
    </h1>

    <p class="studio-description">
      Upload an image, choose your output language,
      and let ARRAI generate a multilingual caption
      using fine-tuned ClipCap.
    </p>

  </div>

</div>
""",
        unsafe_allow_html=True,
    )


def _render_right_empty() -> None:
    """Empty state untuk right panel saat belum ada gambar."""

    st.markdown(
        """
<div class="studio-empty">

  <div class="studio-empty-icon">🖼</div>

  <div class="studio-empty-title">
    No image yet
  </div>

  <div class="studio-empty-description">
    Upload an image on the left to start generating
    multilingual captions.
  </div>

</div>
""",
        unsafe_allow_html=True,
    )


def _render_image_info(uploaded) -> None:
    """Tampilkan metadata file gambar di bawah preview."""

    size_kb = round(uploaded.size / 1024, 1)
    file_type = uploaded.type.split("/")[-1].upper()

    st.markdown(
        f"""
<div class="image-info-bar">

  <div class="image-info-item">
    <span class="image-info-label">File</span>
    <span class="image-info-value">{uploaded.name}</span>
  </div>

  <div class="image-info-item">
    <span class="image-info-label">Type</span>
    <span class="image-info-value">{file_type}</span>
  </div>

  <div class="image-info-item">
    <span class="image-info-label">Size</span>
    <span class="image-info-value">{size_kb} KB</span>
  </div>

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# PUBLIC
# ==========================================================

def render_workspace() -> tuple[Any, str, str, bool]:
    """
    Render Caption Studio Workspace.

    Returns
    -------
    uploaded_file
    language_name
    language_code
    generate_clicked
    """

    _render_page_header()

    st.markdown(
        '<div class="studio-divider"></div>',
        unsafe_allow_html=True,
    )

    # ── Two-column workspace ──────────────────────────────
    left, right = st.columns(
        [1.4, 0.6],
        gap="large",
    )

    uploaded      = None
    language_name = "English"
    language_code = "en"
    generate      = False

    # ── LEFT: upload + preview + info ────────────────────
    with left:

        st.markdown(
            '<div class="panel-label">IMAGE</div>',
            unsafe_allow_html=True,
        )

        uploaded = render_upload_panel()

        if uploaded is not None:

            st.markdown("<br>", unsafe_allow_html=True)

            render_preview_panel(uploaded)

            _render_image_info(uploaded)

    # ── RIGHT: language + generate (or empty state) ──────
    with right:

        st.markdown(
            '<div class="panel-label">SETTINGS</div>',
            unsafe_allow_html=True,
        )

        if uploaded is None:

            _render_right_empty()

        else:

            language_name, language_code = render_language_panel()

            st.markdown("<br>", unsafe_allow_html=True)

            generate = render_generate_panel()

            st.markdown(
                """
<div class="generate-hint">
  AI will generate an English caption,
  then translate it into your selected language.
</div>
""",
                unsafe_allow_html=True,
            )

    return (
        uploaded,
        language_name,
        language_code,
        generate,
    )