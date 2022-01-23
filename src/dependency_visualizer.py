import spacy_streamlit
import streamlit as st
from .utils import load_data_pandas, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    packages = ["spaCy", "NLTK"]

    st.title("Dependency Parsing")
    st.subheader("What type of NLP package would like to explore?")
    pkg_text = st.selectbox("NLP package:", packages)
    st.markdown("---")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')
    doc = spacy_streamlit.process_text(model_name, text)

    if pkg_text == "spaCy":
        spacy_streamlit.visualize_parser(doc, title="Dependency Visualizer")
    elif pkg_text == "NLTK":
        st.write('Placeholder')

