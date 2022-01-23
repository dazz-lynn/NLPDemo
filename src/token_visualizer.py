import spacy_streamlit
import streamlit as st
import spacy
import nltk
import webbrowser
from .utils import load_data_pandas, load_model, load_data_json

def app():
    st.title("Tokenization")
    with st.expander("See explanation"):
        add_desc_ = st.markdown('Tokenization is a way of separating a piece of text into smaller units called '
                                        'tokens. Here, tokens can be either words, characters, or subwords. Hence, '
                                        'tokenization can be broadly classified into 3 types – word, character, '
                                        'and subword (n-gram characters) tokenization. It is a fundamental step in both '
                                        'traditional and deep-learning NLP pipelines.')
        url = 'https://spacy.io/api/tokenizer'
        if st.button('spaCy'):
            webbrowser.open_new_tab(url)

    model_name = "en_core_web_sm"
    packages = ["spaCy", "NLTK"]
    nlp = spacy.load(model_name)

    col1, col2 = st.columns(2)
    with col1:
        with st.container:
            st.subheader("What NLP package would you like to explore?")
    with col2:
        with st.container:
            side_ = st.checkbox("Display side by side")
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