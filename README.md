# ClipCap — AI Image Captioning Web App

Research demo untuk model ClipCap yang di-pretrain pada MS COCO 2017
dan di-fine-tune pada dataset lokal Indonesia (191 gambar, 5 kategori).

## Cara Menjalankan

### 1. Install dependencies

```bash
pip install -r requirements.txt
pip install git+https://github.com/openai/CLIP.git
```

### 2. Letakkan checkpoint model

```
models/clipcap_finetuned_local.pth   ← ~600MB, tidak di-commit ke Git
```

### 3. Jalankan prototype dulu (validasi pipeline)

```bash
streamlit run prototype_test.py
```

### 4. Jalankan aplikasi penuh (setelah UI selesai)

```bash
streamlit run app.py
```

## Struktur Project

```
AI-Captioning-WebApp/
├── app.py                     ← Entry point utama
├── prototype_test.py          ← Pipeline validation prototype
├── config.py                  ← Semua path & konstanta
├── pages/                     ← Multi-page Streamlit
├── utils/
│   ├── load_model.py          ← @st.cache_resource loader
│   ├── inference.py           ← generate_caption()
│   ├── translator.py          ← Independent translation module
│   └── helpers.py             ← Utilitas umum
├── components/                ← Reusable UI components
├── styles/                    ← Custom CSS
├── architecture/
│   └── model_architecture.py  ← TransformerMapper + MLPMapper
└── data/
    └── eval_local.json        ← Hasil evaluasi
```

## Model

- Base: CLIP ViT-B/32 + GPT-2
- Mapper: TransformerMapper (8 layers, 8 heads, prefix_len=10)
- Fine-tuning: Dataset lokal Indonesia, freeze GPT-2, only mapper trained
- BLEU-1: 18.76 | BLEU-4: 7.45 | METEOR: 31.23

## Bahasa Output yang Didukung

🇬🇧 English | 🇮🇩 Indonesian | 🇯🇵 Japanese | 🇸🇦 Arabic | 🇨🇳 Chinese (Simplified)

## Author

Ayu — Universitas Halu Oleo (UHO), Kendari, Indonesia
