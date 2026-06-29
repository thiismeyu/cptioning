"""
components/layout/footer.py

ARRAI Premium Footer
"""

from __future__ import annotations

import streamlit as st


_VERSION = "v1.0.0"
_YEAR    = "2026"

_LINKS = [
    ("Home",           "pages/1_Home.py"),
    ("Caption Studio", "pages/2_Caption_Generator.py"),
    ("Evaluation",     "pages/3_Evaluation.py"),
    ("About",          "pages/4_About.py"),
]


# ==========================================================
# PRIVATE
# ==========================================================

def _render_top() -> None:

    st.markdown(
        f"""<div class="footer-top">
  <div class="footer-brand">
    <div class="footer-logo-row"><div class="footer-logo-icon">⬡</div><div class="footer-logo-name">ARRAI</div></div>
    <p class="footer-description">Multilingual AI image captioning powered by ClipCap — CLIP Vision Encoder, Transformer Mapper, GPT-2, and Deep Translator.</p>
    <div class="footer-badge">Research · Universitas Halu Oleo · {_VERSION}</div>
  </div>
</div>""",
        unsafe_allow_html=True,
    )


def _render_links() -> None:

    cols = st.columns(len(_LINKS), gap="small")

    for col, (title, page) in zip(cols, _LINKS):

        with col:

            if st.button(
                title,
                key=f"footer_{title}",
                use_container_width=True,
            ):
                st.switch_page(page)


def _render_bottom() -> None:

    st.markdown(
        f"""
<div class="footer-bottom">
  <span>© {_YEAR} ARRAI • ClipCap AI Platform</span>
  <span class="footer-bottom-right">
    Built with Streamlit · PyTorch · CLIP · GPT-2
  </span>
</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# PUBLIC
# ==========================================================

def render_footer() -> None:

    st.markdown('<div class="footer">', unsafe_allow_html=True)

    _render_top()

    st.markdown(
        '<div class="footer-nav-label">Navigate</div>',
        unsafe_allow_html=True,
    )

    _render_links()

    _render_bottom()

    st.markdown('</div>', unsafe_allow_html=True)