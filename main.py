import streamlit as st
from src import ner_visualizer, dependency_visualizer, home_page, pos_tagger, token_visualizer

st.set_page_config(layout="wide")

pages = {
    "Introduction": home_page,
    "Tokenization": token_visualizer,
    "POS Tagging": pos_tagger,
    "Dependency Parsing": dependency_visualizer,
    "Named Entity Recognition": ner_visualizer,
}

st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to:", list(pages.keys()))
page = pages[page_selection]
page.app()
