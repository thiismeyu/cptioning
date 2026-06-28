"""
components/ui/badge.py
"""

from __future__ import annotations

import streamlit as st


def badge(
    text: str,
    *,
    color: str = "green",
) -> None:

    st.markdown(
        f"""
<div class="badge">

<span class="badge-dot"></span>

{text}

</div>
""",
        unsafe_allow_html=True,
    )