from transformers import pipeline

MODEL_MAP = {
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
    ("en", "ml"): "Helsinki-NLP/opus-mt-en-ml",
}

def get_translator(src_lang, tgt_lang):
    model_name = MODEL_MAP.get((src_lang, tgt_lang))
    if not model_name:
        raise ValueError(f"Translation model not available for {src_lang} → {tgt_lang}")
    return pipeline("translation", model=model_name)

def translate_text(translator, text):
    return translator(text)[0]['translation_text']
