"""
components/sections/hero.py
ARRAI Hero Section
"""
from __future__ import annotations
from pathlib import Path
import streamlit as st
from components.ui.badge import badge
from components.ui.button import primary_button, secondary_button
from components.ui.tag import tags

_LOGO_PATH = Path(__file__).resolve().parents[2] / "assets" / "logo" / "arrai_logo.png"

_METRICS = [
    ("Models",    "4"),
    ("Languages", "5"),
    ("BLEU-1",    "18.76"),
    ("METEOR",    "31.23"),
]

_TAGS = [
    "CLIP ViT-B/32", "Transformer", "GPT-2",
    "Deep Translator", "Fine-tuned", "Research Grade",
]

_PIPELINE = [
    ("🖼️", "Image Input",   "Upload PNG/JPG"),
    ("🧠", "CLIP",          "Vision Encoder"),
    ("⚙️", "Mapper",        "Transformer"),
    ("💬", "GPT-2",         "Language Model"),
    ("🌍", "Translate",     "5 Languages"),
    ("✅", "Caption",       "Output"),
]


def _render_left() -> None:

    if _LOGO_PATH.exists():
        st.image(str(_LOGO_PATH), width=72)
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    badge("Research Grade AI Platform")

    st.markdown("""
<h1 style="
    font-size: clamp(2.8rem, 4.5vw, 4.4rem);
    font-weight: 900;
    letter-spacing: -.05em;
    line-height: 1.05;
    color: #F5F7FA;
    margin: 12px 0 20px;
">
    Understanding Images.<br>
    <span style="
        background: linear-gradient(135deg, #6D5DF6, #27C5FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    ">Beyond Pixels.</span>
</h1>
<p style="
    color: #B7C0CE;
    font-size: 1rem;
    line-height: 1.85;
    max-width: 580px;
    margin-bottom: 2rem;
">
    ARRAI generates natural, multilingual image captions using
    a fine-tuned ClipCap architecture — CLIP Vision Encoder,
    Transformer Mapper, GPT-2 Language Model, and Deep Translator
    — in one unified pipeline.
</p>
""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="small")
    with col1:
        primary_button("🚀 Launch Studio", "pages/2_Caption_Generator.py", "hero_launch")
    with col2:
        secondary_button("Research →", "pages/4_About.py", "hero_about")

    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)

    # Metrics
    metric_cols = st.columns(len(_METRICS))
    for col, (label, value) in zip(metric_cols, _METRICS):
        with col:
            st.markdown(f"""
<div style="text-align:center; padding: 16px 8px;">
    <div style="
        font-size: .68rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .10em;
        color: #8E98A8;
        margin-bottom: 6px;
    ">{label}</div>
    <div style="
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -.03em;
        background: linear-gradient(135deg, #6D5DF6, #27C5FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    ">{value}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
    tags(_TAGS)


def _render_right() -> None:

    nodes_html = ""
    for i, (icon, name, subtitle) in enumerate(_PIPELINE):
        is_last = i == len(_PIPELINE) - 1
        border_color = "rgba(46,204,113,.25)" if is_last else "rgba(255,255,255,.07)"
        bg_color = "rgba(46,204,113,.04)" if is_last else "rgba(255,255,255,.03)"
        icon_bg = "rgba(46,204,113,.12)" if is_last else "rgba(109,93,246,.10)"

        nodes_html += f"""
<div style="
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 12px 16px;
    border-radius: 14px;
    background: {bg_color};
    border: 1px solid {border_color};
    margin-bottom: 8px;
    transition: border-color .2s, transform .2s;
">
    <div style="
        width: 42px; height: 42px;
        border-radius: 12px;
        background: {icon_bg};
        display: flex; align-items: center; justify-content: center;
        font-size: 20px;
        flex-shrink: 0;
    ">{icon}</div>
    <div>
        <div style="font-size:.9rem;font-weight:700;color:#F5F7FA;line-height:1;">{name}</div>
        <div style="font-size:.76rem;color:#8E98A8;margin-top:3px;">{subtitle}</div>
    </div>
</div>
"""
        if not is_last:
            nodes_html += """
<div style="
    text-align:center;
    font-size:14px;
    color:#27C5FF;
    opacity:.4;
    margin: 2px 0;
    padding-left: 20px;
">↓</div>
"""

    st.markdown(f"""
<div style="
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 24px;
    padding: 28px 24px;
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
">
    <div style="
        position: absolute; top: 0; right: 0;
        width: 200px; height: 200px;
        background: radial-gradient(circle at top right, rgba(109,93,246,.10), transparent 70%);
        pointer-events: none;
    "></div>

    <div style="
        display:inline-flex; align-items:center; gap:8px;
        padding: 5px 12px;
        border-radius: 999px;
        background: rgba(109,93,246,.10);
        border: 1px solid rgba(109,93,246,.20);
        font-size:.65rem; font-weight:800;
        letter-spacing:.12em; color:#8E81FF;
        text-transform:uppercase;
        margin-bottom:14px;
    ">AI PIPELINE</div>

    <h3 style="
        font-size:1.15rem; font-weight:800;
        color:#F5F7FA; margin-bottom:8px;
        letter-spacing:-.02em; line-height:1.2;
    ">Multilingual Caption Generation</h3>

    <p style="
        color:#8E98A8; font-size:.84rem;
        line-height:1.65; margin-bottom:20px;
    ">From image understanding to natural language output.</p>

    {nodes_html}
</div>
""", unsafe_allow_html=True)


def render_hero() -> None:

    st.markdown("""
<div style="
    position: relative;
    padding: 3rem 0 1rem;
    overflow: hidden;
">
    <div style="
        position: absolute; top: -200px; left: -180px;
        width: 500px; height: 500px; border-radius: 50%;
        background: radial-gradient(circle, rgba(109,93,246,.18), transparent 70%);
        pointer-events: none;
    "></div>
    <div style="
        position: absolute; top: 60px; right: -160px;
        width: 440px; height: 440px; border-radius: 50%;
        background: radial-gradient(circle, rgba(39,197,255,.12), transparent 70%);
        pointer-events: none;
    "></div>
</div>
""", unsafe_allow_html=True)

    left, right = st.columns([1.3, 0.7], gap="large")
    with left:
        _render_left()
    with right:
        _render_right()

    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)