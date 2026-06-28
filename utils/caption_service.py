"""
utils/caption_service.py

ARRAI Caption Service
"""

from __future__ import annotations

from utils.inference import generate_caption
from utils.translator import translate


def generate(
    *,
    image,
    bundle,
    language_code: str,
):
    """
    Generate multilingual caption.
    """

    caption, elapsed = generate_caption(
        image=image,
        bundle=bundle,
    )

    translated = translate(
        caption,
        language_code,
    )

    return {
        "caption": caption,
        "translation": translated,
        "elapsed": elapsed,
    }