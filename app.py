import streamlit as st
from translator import get_translator, translate_text

st.set_page_config(page_title="🌍 Language Translator", layout="centered")
st.title("🌍 Language Translator")

# Language name-code map
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Malayalam": "ml"
}

# Dropdowns for language selection
src_lang = st.selectbox("Source Language", list(languages.keys()))
tgt_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

# Text input
text = st.text_area("Enter text to translate:")

# Translate button
if st.button("Translate"):
    try:
        src_code = languages[src_lang]
        tgt_code = languages[tgt_lang]
        translator = get_translator(src_code, tgt_code)
        translated_text = translate_text(translator, text)
        st.success(translated_text)
    except Exception as e:
        st.error(f"Error: {e}")
