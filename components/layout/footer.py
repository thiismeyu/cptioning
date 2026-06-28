"""
components/layout/footer.py

ARRAI Footer
"""

from __future__ import annotations

import streamlit as st


_VERSION = "v1.0.0"

_YEAR = "2026"

_LINKS = [

    ("Home", "pages/1_Home.py"),

    ("Caption Studio", "pages/2_Caption_Generator.py"),

    ("Evaluation", "pages/3_Evaluation.py"),

    ("About", "pages/4_About.py"),

]
# ==========================================================
# FOOTER
# ==========================================================

def _render_footer() -> None:

    st.markdown(
        f"""
<div class="footer">

<div class="footer-top">

<div>

<div class="footer-logo">

ARRAI

</div>

<div class="footer-subtitle">

Premium Multilingual Image Captioning Platform

</div>

</div>

<div class="footer-version">

{_VERSION}

</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    cols = st.columns(len(_LINKS))

    for col, (title, page) in zip(cols, _LINKS):

        with col:

            if st.button(

                title,

                key=f"footer_{title}",

                use_container_width=True,

            ):

                st.switch_page(page)
# ==========================================================
# PUBLIC
# ==========================================================

def render_footer() -> None:

    _render_footer()

    st.markdown(
        f"""
<div class="footer-bottom">

© {_YEAR} ARRAI • ClipCap AI Platform

</div>
""",
        unsafe_allow_html=True,
    )