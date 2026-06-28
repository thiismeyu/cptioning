"""
components/sections/hero.py

ARRAI Hero Section
"""

from __future__ import annotations

import streamlit as st

from components.ui.badge import badge
from components.ui.button import (
    primary_button,
    secondary_button,
)
from components.ui.metric import metric_row
from components.ui.tag import tags


# ==========================================================
# CONFIG
# ==========================================================

_TITLE = """
Understanding Images.
Beyond Pixels.
"""

_DESCRIPTION = """
ARRAI is a premium AI platform capable of generating
natural multilingual image captions using a fine-tuned
ClipCap architecture combining CLIP Vision Encoder,
Transformer Mapper, GPT-2 Language Model,
and Deep Translator.
"""

_METRICS = [

    ("Models", "4"),

    ("Languages", "5"),

    ("BLEU", "0.84"),

    ("CIDEr", "1.16"),

]

_TAGS = [

    "CLIP ViT-B/32",

    "Transformer",

    "GPT-2",

    "Deep Translator",

    "Research Grade",

]

_PIPELINE = [

    ("🖼", "Image", "Input"),

    ("🧠", "CLIP", "Vision Encoder"),

    ("⚙", "Mapper", "Transformer"),

    ("💬", "GPT-2", "Language Model"),

    ("🌍", "Translate", "5 Languages"),

    ("✅", "Caption", "Output"),

]


# ==========================================================
# LEFT
# ==========================================================

def _render_left() -> None:

    badge(
        "Research Grade AI Platform"
    )

    st.markdown(
        f"""
<h1 class="hero-title">

{_TITLE.replace(".", ".<br>")}

</h1>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<p class="hero-description">

{_DESCRIPTION}

</p>
""",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        primary_button(

            label="Launch Studio",
            page="pages/2_Caption_Generator.py",
            key="hero_launch",  
        )

    with col2:

        secondary_button(

            label="Research",
            page="pages/4_About.py",
            key="hero_about",

        )

    st.markdown("<br>", unsafe_allow_html=True)

    metric_row(_METRICS)

    st.markdown("<br>", unsafe_allow_html=True)

    tags(_TAGS)

# ==========================================================
# PIPELINE
# ==========================================================

def _pipeline_html() -> str:

    html = """
<div class="pipeline-card">

<div class="pipeline-header">

<div class="pipeline-label">

AI Pipeline

</div>

<h3>

Multilingual Caption Generation

</h3>

<p>

From image understanding to natural language generation.

</p>

</div>

<div class="pipeline-flow">

"""

    last = len(_PIPELINE) - 1

    for index, (icon, title, subtitle) in enumerate(_PIPELINE):

        active = " pipeline-node-success" if index == last else ""

        html += f"""

<div class="pipeline-node{active}">

<div class="pipeline-icon">

{icon}

</div>

<div class="pipeline-name">

{title}

</div>

<div class="pipeline-subtitle">

{subtitle}

</div>

</div>

"""

        if index != last:

            html += """

<div class="pipeline-arrow">

↓

</div>

"""

    html += """

</div>

</div>

"""

    return html


# ==========================================================
# RIGHT
# ==========================================================

def _render_right() -> None:

    st.markdown(

        _pipeline_html(),

        unsafe_allow_html=True,

    )
# ==========================================================
# HERO LAYOUT
# ==========================================================

def _render_content() -> None:

    left, right = st.columns(
        [1.25, 0.75],
        gap="large",
    )

    with left:

        _render_left()

    with right:

        _render_right()


def _render_background() -> None:

    st.markdown(
        """
<div class="hero-background">

<div class="hero-blur hero-blur-left"></div>

<div class="hero-blur hero-blur-right"></div>

</div>
""",
        unsafe_allow_html=True,
    )


def _render_divider() -> None:

    st.markdown(
        """
<div class="hero-divider"></div>
""",
        unsafe_allow_html=True,
    )


def _render_spacing() -> None:

    st.markdown(
        """
<div class="hero-spacing"></div>
""",
        unsafe_allow_html=True,
    )
    
# ==========================================================
# PUBLIC
# ==========================================================

def render_hero() -> None:
    """
    Render ARRAI Hero Section.
    """

    _render_background()

    _render_content()

    _render_spacing()

    _render_divider()