"""
components/about/roadmap.py
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


_ITEMS = [

    ("✅", "ClipCap Fine-tuning"),

    ("✅", "Multilingual Translation"),

    ("✅", "Modern UI"),

    ("🔄", "Continuous Improvement"),

]


def render_roadmap():

    section_title(
        "Development Status",
        "Current progress of the ARRAI project.",
    )

    html = '<div class="model-card">'

    for icon, item in _ITEMS:

        html += f"""

<div class="model-item">

<div class="model-label">

{icon} {item}

</div>

<div class="model-value">

Completed

</div>

</div>

"""

    html += "</div>"

    st.markdown(
        html,
        unsafe_allow_html=True,
    )