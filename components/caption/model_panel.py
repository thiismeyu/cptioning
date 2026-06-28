"""
components/caption/model_panel.py

ARRAI Premium Model Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


def render_model_panel(
    model_info: dict,
) -> None:
    """
    Render model information.
    """

    section_title(
        "Model Information",
        "Current AI model configuration.",
    )

    if not model_info:

        st.info("No model information available.")

        return

    html = """
<div class="model-card">
"""

    for key, value in model_info.items():

        html += f"""
<div class="model-item">

<div class="model-label">

{key}

</div>

<div class="model-value">

{value}

</div>

</div>
"""

    html += """
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True,
    )