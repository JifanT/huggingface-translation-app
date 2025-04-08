import streamlit as st
from translator import get_translator, translate_text
# Language codes and names
languages = {
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Hindi": "hi",
    "Malayalam": "ml"
}
st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌍 Language Translator")
# Language selection
src_lang_name = st.selectbox("Source Language", list(languages.keys()))
tgt_lang_name = st.selectbox("Target Language", list(languages.keys()))
src = languages[src_lang_name]
tgt = languages[tgt_lang_name]
text = st.text_area("Enter text to translate:")
if st.button("Translate"):
    if src == tgt:
        st.warning("Source and target languages are the same!")
    elif not text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            translator = get_translator(src, tgt)
            translated = translate_text(translator, text)
            st.success("Translation:")
            st.write(translated)
        except Exception as e:
            st.error(f"Error: {e}")