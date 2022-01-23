import streamlit as st
from src import ner_visualizer, dependency_visualizer, home_page, pos_tagger

pages = {
    "Introduction": home_page,
    "POS Tagging": pos_tagger,
    "Named Entity Recognition": ner_visualizer,
    "Token Analysis & Dependency Visualizer": dependency_visualizer,
}

st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to:", list(pages.keys()))
page = pages[page_selection]
page.app()
