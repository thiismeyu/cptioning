"""
components/empty_state.py

ARRAI Empty State
"""

from __future__ import annotations

import streamlit as st


def render_empty_state() -> None:
    """
    Empty state shown before an image is uploaded.
    """

    st.markdown(
        """
<div class="empty-state">

<div class="empty-icon">

🖼️

</div>

<div class="empty-title">

No Image Selected

</div>

<div class="empty-description">

Upload an image to generate multilingual captions
using the fine-tuned ClipCap AI model.

</div>

</div>
""",
        unsafe_allow_html=True,
    )