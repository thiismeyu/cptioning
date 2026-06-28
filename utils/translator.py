"""
utils/translator.py

Independent translation module.
Interface publik: translate(text, target_lang_code) -> str

Module ini SENGAJA dibuat self-contained:
  - Tidak ada import dari module lain di project ini
  - Hanya import dari config untuk SUPPORTED_LANGUAGES
  - Bisa diganti dengan implementasi lain (Argos, DeepL, dll.)
    tanpa menyentuh file apapun selain file ini

Backend saat ini: deep-translator (Google Translate wrapper)
  - Gratis, tidak perlu API key
  - Rate limit: ~1000 request/hari untuk free tier

Cara ganti backend:
  1. Ganti fungsi _translate_with_google() dengan implementasi baru
  2. Jangan ubah signature translate() — itu adalah kontrak publik
"""

import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# SUPPORTED LANGUAGES
# Disalin dari config untuk menjaga module ini independent
# ─────────────────────────────────────────────
SUPPORTED_LANGUAGES: dict[str, str] = {
    "English": "en",
    "Indonesian": "id",
    "Japanese": "ja",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN",
}

# Reverse mapping: kode → nama
LANG_CODE_TO_NAME: dict[str, str] = {v: k for k, v in SUPPORTED_LANGUAGES.items()}

# Flag emoji untuk tiap bahasa (untuk UI)
LANGUAGE_FLAGS: dict[str, str] = {
    "en": "🇬🇧",
    "id": "🇮🇩",
    "ja": "🇯🇵",
    "ar": "🇸🇦",
    "zh-CN": "🇨🇳",
}


# ─────────────────────────────────────────────
# INTERNAL BACKEND
# ─────────────────────────────────────────────
def _translate_with_google(text: str, target: str) -> str:
    """
    Backend: Google Translate via deep-translator.
    Ganti fungsi ini untuk mengganti backend.
    """
    from deep_translator import GoogleTranslator
    result = GoogleTranslator(source="en", target=target).translate(text)
    return result if result else text


# ─────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────
def translate(
    text: str,
    target_lang_code: str,
    source_lang_code: str = "en",
    retries: int = 2,
    retry_delay: float = 1.0,
) -> str:
    """
    Terjemahkan teks ke bahasa target.

    Args:
        text: teks bahasa Inggris yang akan diterjemahkan
        target_lang_code: kode bahasa target ("id", "ja", "ar", "zh-CN", "en")
        source_lang_code: kode bahasa sumber (default "en")
        retries: jumlah percobaan ulang jika gagal
        retry_delay: jeda antar percobaan (detik)

    Returns:
        Teks terjemahan. Jika gagal, kembalikan teks asli.

    Catatan:
        Jika target == source, teks dikembalikan langsung tanpa API call.
    """
    if not text or not text.strip():
        return text

    # Tidak perlu translate jika bahasa sama
    if target_lang_code == source_lang_code or target_lang_code == "en":
        logger.debug(f"Skip translate: target sama dengan source ({target_lang_code})")
        return text

    last_error: Optional[Exception] = None

    for attempt in range(1, retries + 1):
        try:
            logger.info(
                f"Translate [{source_lang_code}→{target_lang_code}] "
                f"attempt {attempt}/{retries}: {text[:50]}..."
            )
            result = _translate_with_google(text, target_lang_code)
            logger.info(f"Translate sukses: {result[:50]}...")
            return result

        except Exception as e:
            last_error = e
            logger.warning(f"Translate gagal (attempt {attempt}): {e}")
            if attempt < retries:
                time.sleep(retry_delay)

    # Semua attempt gagal — kembalikan teks asli dengan log warning
    logger.error(
        f"Semua {retries} attempt translate gagal. "
        f"Mengembalikan teks asli. Error terakhir: {last_error}"
    )
    return text


def translate_to_all_languages(text: str) -> dict[str, str]:
    """
    Terjemahkan satu teks ke semua bahasa yang didukung.
    Digunakan di halaman Examples.

    Returns:
        dict: {"en": "...", "id": "...", "ja": "...", "ar": "...", "zh-CN": "..."}
    """
    results = {}
    for lang_name, lang_code in SUPPORTED_LANGUAGES.items():
        results[lang_code] = translate(text, lang_code)
    return results


def get_language_display_name(lang_code: str) -> str:
    """Kembalikan nama tampilan dari kode bahasa."""
    return LANG_CODE_TO_NAME.get(lang_code, lang_code)


def get_language_flag(lang_code: str) -> str:
    """Kembalikan emoji flag untuk kode bahasa."""
    return LANGUAGE_FLAGS.get(lang_code, "🌐")
