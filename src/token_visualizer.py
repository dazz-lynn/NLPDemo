import spacy_streamlit
import streamlit as st
import spacy
import nltk
from .utils import load_data_pandas, load_model, load_data_json

def app():
    model_name = "en_core_web_sm"
    packages = ["spaCy", "NLTK"]

    nlp = spacy.load(model_name)

    st.title("Tokenization")
    st.subheader("What type of NLP package would like to explore?")
    pkg_text = st.selectbox("NLP package:", packages)
    st.markdown("---")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')

    if pkg_text == "spaCy":
        doc = nlp(text)

        spacy_streamlit.visualize_tokens(
            doc,
            attrs=["text", "pos_", "dep_", "ent_type_"]
        )
    elif pkg_text == "NLTK":
        st.write(nltk.tokenize.word_tokenize(text))