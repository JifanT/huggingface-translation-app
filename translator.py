from transformers import pipeline

def get_translator(src_lang="en", tgt_lang="fr"):
    try:
        model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
        translator = pipeline("translation", model=model_name)
        return translator
    except Exception:
        raise Exception(f"Translation model not available for {src_lang} → {tgt_lang}")

def translate_text(translator, text):
    result = translator(text, max_length=400)
    return result[0]['translation_text']
