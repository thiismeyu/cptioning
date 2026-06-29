"""
components/caption/loading_panel.py

ARRAI Loading Panel
"""

from __future__ import annotations

import streamlit as st


def render_loading_panel():

    st.markdown(
        """<div class="glass fade-up">
<h3 style="text-align:center;">🧠 Generating Caption</h3>
<p style="text-align:center;color:var(--text-secondary);">AI is analyzing your image...</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.progress(0)