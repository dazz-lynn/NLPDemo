import spacy_streamlit
import streamlit as st
from .utils import load_data_pandas, load_model, load_data_json
import random


def app():
    model_name = "en_core_web_sm"
    # filepath = "src/reviewSamples20.json"
    # df = load_data_pandas(filepath)
    # reviews = df["text"].to_list()
    packages = ["spaCy", "NLP"]
    # random.seed(420)
    # random.shuffle(reviews)

    nlp = load_model(model_name)

    st.title("Named Entity Recognition")
    st.subheader("What type of NLP package would like to explore?")
    pkg_text = st.selectbox("NLP package:", packages)
    st.markdown("---")

    st.subheader("Enter the text you'd like to analyze.")
    text = st.text_input('Enter text')

    doc = spacy_streamlit.process_text(model_name, text)
    # review_data = load_data_json(filepath, pkg_text)
    # st.markdown("JSON object:")
    # st.json(review_data)

    spacy_streamlit.visualize_ner(
        doc,
        labels=nlp.get_pipe("ner").labels,
        title="Named Entity Recognition Visualizer",
    )
