"""
components/evaluation/conclusion_panel.py

ARRAI Conclusion Panel
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


_TEXT = """
The fine-tuned ClipCap model demonstrates strong performance
across all evaluation metrics. BLEU, ROUGE-L, and CIDEr indicate
that the generated captions closely resemble human-written captions,
while METEOR confirms good semantic similarity.

Overall, ARRAI successfully generates fluent multilingual image
captions suitable for research and real-world applications.
"""


def render_conclusion_panel() -> None:
    """
    Render evaluation conclusion.
    """

    section_title(
        "Evaluation Conclusion",
        "Summary of the experimental results.",
    )

    st.markdown(
        f"""
<div class="glass">

<p class="result-text">

{_TEXT}

</p>

</div>
""",
        unsafe_allow_html=True,
    )