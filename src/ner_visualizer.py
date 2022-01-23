import spacy_streamlit
import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize
from .utils import load_data_pandas, load_model, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    packages = ["spaCy", "NLTK"]

    nlp = load_model(model_name)

    st.title("Named Entity Recognition")
    st.subheader("What type of NLP package would like to explore?")
    pkg_text = st.selectbox("NLP package:", packages)
    st.markdown("---")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')

    if pkg_text == "spaCy":
        doc = spacy_streamlit.process_text(model_name, text)

        spacy_streamlit.visualize_ner(
            doc,
            labels=nlp.get_pipe("ner").labels,
        )
    elif pkg_text == "NLTK":
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        for sent in nltk.sent_tokenize(text):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    if chunk.label() == 'GPE':
                        st.write('GEOPOLITICAL', ' '.join(c[0] for c in chunk))
                    st.write(chunk.label(), ' '. join(c[0] for c in chunk))

