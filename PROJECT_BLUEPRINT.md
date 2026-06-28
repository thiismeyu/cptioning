# AI-Captioning-WebApp — Project Blueprint
# Dibuat sebelum implementasi. Dokumen ini mendefinisikan
# tanggung jawab setiap file secara eksplisit.

## ENTRY POINT
app.py
  - Konfigurasi halaman Streamlit (title, icon, layout="wide")
  - Load CSS dari styles/ (main.css, animations.css, components.css)
  - Render halaman Home: hero section, deskripsi riset, highlight fitur
  - Tidak mengandung logika model atau inference

## PAGES
pages/1_Caption_Generator.py
  - Upload gambar (jpg, jpeg, png, webp)
  - Image preview dengan metadata (ukuran, format)
  - Dropdown pilihan bahasa (5 bahasa)
  - Tombol Generate Caption
  - Tampilkan caption hasil + terjemahan
  - Tampilkan inference time
  - Tombol Copy dan Download .txt
  - Panggil: utils/load_model.py, utils/inference.py, utils/translator.py

pages/2_Examples.py
  - Menampilkan 5–6 sample image dari assets/sample_images/
  - Setiap gambar: tampilkan caption dalam semua 5 bahasa
  - Data caption dari data/sample_captions.json (pre-generated, tidak real-time)
  - Tujuan: demo visual yang cepat tanpa menunggu inference

pages/3_Evaluation.py
  - Baca data/eval_local.json
  - Tampilkan metrik: BLEU-1, BLEU-4, ROUGE-L, METEOR, CIDEr
  - Visualisasi bar chart menggunakan st.bar_chart atau plotly
  - Informasi konteks: ukuran dataset, jumlah test image, epoch training
  - Penjelasan singkat setiap metrik dalam bahasa Indonesia

pages/4_About.py
  - Informasi peneliti / proyek
  - Arsitektur model: CLIP → TransformerMapper → GPT-2
  - Pipeline diagram (markdown / HTML visual)
  - Dataset info: 191 gambar, 5 kategori
  - Bahasa yang didukung
  - Informasi fine-tuning
  - Referensi / credit

## UTILS
utils/load_model.py
  - @st.cache_resource def load_model()
  - Load checkpoint dari models/clipcap_finetuned_local.pth
  - Rebuild TransformerMapper dari config (persis seperti notebook)
  - Load GPT-2 dengan gpt2.load_state_dict(ckpt["gpt2"])
  - Load CLIP ViT-B/32
  - Return: (clip_model, preprocess, mapping_net, gpt2, tokenizer, config, device)
  - Tangani FileNotFoundError dengan pesan yang jelas
  - TIDAK mengubah struktur checkpoint

utils/inference.py
  - def generate_caption(image: PIL.Image, clip_model, preprocess,
                         mapping_net, gpt2, tokenizer, device) -> tuple[str, float]
  - Implementasi persis dari Cell 35 notebook:
      feat = clip_model.encode_image(preprocess(image).unsqueeze(0).to(device))
      prefix = mapping_net(feat.float())
      embeds = cat([prefix, gpt2.transformer.wte(eos_tensor)])
      output = gpt2.generate(inputs_embeds=embeds, num_beams=5,
                             max_new_tokens=60, min_new_tokens=8,
                             no_repeat_ngram_size=3, repetition_penalty=1.2, ...)
  - Return (caption_str, elapsed_seconds)

utils/translator.py
  - INDEPENDENT MODULE — bisa diganti tanpa menyentuh file lain
  - Gunakan deep-translator (GoogleTranslator)
  - SUPPORTED_LANGUAGES dict: {"Indonesian": "id", "English": "en",
    "Japanese": "ja", "Arabic": "ar", "Chinese (Simplified)": "zh-CN"}
  - def translate(text: str, target_lang: str) -> str
  - Jika target == "en": return text langsung (tidak perlu translate)
  - Graceful fallback: jika translate gagal, return teks asli + warning

utils/helpers.py
  - def load_css(filepath: str) -> None  (inject CSS ke Streamlit)
  - def load_css_files(*paths) -> None
  - def format_inference_time(seconds: float) -> str
  - def get_image_info(image: PIL.Image) -> dict
  - def get_model_status() -> dict  (check apakah .pth ada)

## COMPONENTS
components/header.py
  - def render_page_header(title, subtitle, icon)  → st.markdown HTML
  - Gradient header dengan judul halaman

components/footer.py
  - def render_footer()  → st.markdown HTML
  - Credit, versi, nama peneliti

components/sidebar.py
  - def render_sidebar()  → konfigurasi sidebar
  - Logo / nama app, navigasi info, status model

components/cards.py
  - def metric_card(label, value, delta=None)  → st.markdown HTML
  - def info_card(title, content, icon)
  - def caption_result_card(caption, lang, flag)

## STYLES
styles/main.css
  - CSS variables (warna, font, spacing, radius, shadow)
  - Dark / Light mode via @media prefers-color-scheme
  - Typography: Inter font dari Google Fonts
  - Layout: container, section spacing
  - Hero section styling
  - Tombol custom (.btn-primary, .btn-secondary)
  - Input / upload area styling
  - Sidebar styling override

styles/animations.css
  - @keyframes fadeIn, slideUp, pulse, shimmer
  - Loading spinner
  - Hover transitions
  - Caption reveal animation

styles/components.css
  - Card components (.card, .glass-card, .metric-card)
  - Badge / tag styling
  - Language selector
  - Caption output box
  - Divider / separator styles
  - Responsive breakpoints

## ARCHITECTURE
architecture/model_architecture.py
  - Copy persis class TransformerMapper dan MLPMapper dari notebook Cell 4
  - Tidak ada modifikasi apapun
  - Ini satu-satunya sumber kebenaran arsitektur

## DATA
data/eval_local.json
  - Salin dari file yang diupload
  - {"BLEU-1": 18.76, "BLEU-4": 7.45, "ROUGE-L": 23.57,
     "METEOR": 31.23, "CIDEr": 2.08, "avg_len": 44.25,
     "num_test": 20, "caption_field_used": "captions_en"}

data/sample_captions.json
  - Pre-generated captions untuk halaman Examples
  - Format: [{"image": "sample_01.jpg", "category": "Food",
               "captions": {"en": "...", "id": "...", "ja": "...",
                            "ar": "...", "zh": "..."}}]

## CONFIG
.streamlit/config.toml
  - [theme]: primaryColor, backgroundColor, font
  - [server]: maxUploadSize = 10

## ROOT
requirements.txt
  - Semua dependencies dengan versi yang dikunci

.gitignore
  - models/*.pth (jangan push checkpoint 600MB)
  - __pycache__, .env, *.pyc

