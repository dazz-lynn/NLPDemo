import spacy_streamlit
import streamlit as st
import nltk
import spacy
from spacy import displacy
from .utils import load_data_pandas, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    nlp = spacy.load(model_name)
    packages = ["spaCy", "NLTK"]

    st.title("Part Of Speech Tagging")
    st.subheader("What type of NLP package would like to explore?")
    pkg_text = st.selectbox("NLP package:", packages)
    st.markdown("---")
    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')

    HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; 
    margin-bottom: 2.5rem">{}</div> """

    if pkg_text == "spaCy":
        if text != "":
            doc = nlp(text)
            for token in doc:
                st.markdown(token, token.pos_)

            # USEFUL FOR DISPLAYING USING RAW HTML
            # if "parser" in nlp.pipe_names:
            #     st.subheader("Dependency Parse & Part-of-speech tags")
            #     st.sidebar.header("Dependency Parse")
            #     split_sents = st.sidebar.checkbox("Split sentences", value=True)
            #     collapse_punct = st.sidebar.checkbox("Collapse punctuation", value=True)
            #     collapse_phrases = st.sidebar.checkbox("Collapse phrases")
            #     compact = st.sidebar.checkbox("Compact mode")
            #     options = {
            #         "collapse_punct": collapse_punct,
            #         "collapse_phrases": collapse_phrases,
            #         "compact": compact,
            #     }
            # docs = [span.as_doc() for span in doc.sents] if split_sents else [doc]
            # for sent in docs:
            #     html = displacy.render(sent, options=options)
            #     # Double newlines seem to mess with the rendering
            #     html = html.replace("\n\n", "\n")
            #     if split_sents and len(docs) > 1:
            #         st.markdown(f"> {sent.text}")
            #     st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    elif pkg_text == "NLTK":
        token_list = nltk.pos_tag(nltk.word_tokenize(text))
        for pair in token_list:
            st.write(pair)

