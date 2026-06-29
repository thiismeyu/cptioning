"""
components/caption/result_panel.py

ARRAI Premium Result Panel
Menampilkan caption bahasa Inggris + terjemahan dengan styling premium.
"""

from __future__ import annotations

import streamlit as st

from components.ui.section import section_title


# ==========================================================
# PRIVATE — HTML BUILDERS
# ==========================================================

def _caption_html(
    badge_emoji: str,
    label: str,
    caption: str,
    accent: bool = False,
) -> str:
    """
    Bangun satu result card sebagai raw HTML.
    accent=True → border primary glow untuk translation card.
    """

    accent_class = " result-card-accent" if accent else ""

    return (
        f'<div class="result-card{accent_class}">'
        f'<div class="result-header">'
        f'<div class="result-badge">{badge_emoji}</div>'
        f'<div class="result-header-text"><div class="result-label">{label}</div></div>'
        f'</div>'
        f'<div class="result-text">{caption}</div>'
        f'</div>'
    )


def _copy_hint_html(caption: str) -> str:
    """
    Teks kecil hint untuk copy caption.
    Streamlit tidak support clipboard JS secara native,
    jadi kita tampilkan teks yang bisa di-select user.
    """
    return f"""
<div class="result-copy-hint">
  Click text di bawah untuk select &amp; copy
</div>
<div class="result-copy-box">
  {caption}
</div>
"""


# ==========================================================
# PUBLIC
# ==========================================================

def render_result_panel(
    english_caption: str,
    translated_caption: str,
    language_name: str,
    language_flag: str,
) -> None:
    """
    Render result panel dengan dua kartu:
    - English caption (selalu ada)
    - Translated caption (ditampilkan jika berbeda dari English)

    Parameters
    ----------
    english_caption : str
        Caption dalam bahasa Inggris dari GPT-2.
    translated_caption : str
        Caption setelah diproses Deep Translator.
    language_name : str
        Nama bahasa output yang dipilih user (e.g. "Indonesian").
    language_flag : str
        Emoji flag bahasa (e.g. "🇮🇩").
    """

    section_title(
        "Caption Result",
        "AI-generated caption ready to use.",
    )

    # ── English caption card ──────────────────────────────
    st.markdown(
        _caption_html(
            badge_emoji="🇬🇧",
            label="English Caption",
            caption=english_caption,
        ),
        unsafe_allow_html=True,
    )

    # ── Translation card (hanya tampil jika bukan English) ─
    if language_name != "English" and translated_caption:

        st.markdown(
            _caption_html(
                badge_emoji=language_flag,
                label=f"{language_name} Translation",
                caption=translated_caption,
                accent=True,
            ),
            unsafe_allow_html=True,
        )

    # ── Copy hint ─────────────────────────────────────────
    display_caption = (
        translated_caption
        if language_name != "English" and translated_caption
        else english_caption
    )

    with st.expander("📋 Select & Copy Caption", expanded=False):
        st.code(display_caption, language=None)