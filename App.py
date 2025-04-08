import streamlit as st
from translator import get_translator, translate_text

# UI
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")
st.title("🌍 Language Translator")

# Language map
language_names = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "hi": "Hindi",
    "ml": "Malayalam"
}

# Reverse map for dropdowns
name_to_code = {v: k for k, v in language_names.items()}

src_lang_name = st.selectbox("Source Language", list(language_names.values()), index=0)
tgt_lang_name = st.selectbox("Target Language", list(language_names.values()), index=1)

text_to_translate = st.text_area("Enter text to translate:")

if st.button("Translate"):
    try:
        src = name_to_code[src_lang_name]
        tgt = name_to_code[tgt_lang_name]
        translator = get_translator(src, tgt)
        result = translate_text(translator, text_to_translate)
        st.success(result)
    except Exception as e:
        st.error(f"Error: {str(e)}")
