"""
components/caption/preview_panel.py
"""

from __future__ import annotations

from PIL import Image

import streamlit as st

from components.ui.section import section_title


def render_preview_panel(
    image: Image.Image,
) -> None:

    section_title(
        "Image Preview",
        "Uploaded image ready for caption generation.",
    )

    st.image(
        image,
        use_container_width=True,
    )