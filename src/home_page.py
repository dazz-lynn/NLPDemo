import streamlit as st


def app():
    st.markdown(
        """
# Natural Language Processing Demo

As part of the High Fidelity prototyping phase, 
a Streamlit application is used to partially explore and visualise the final website.

The features prototyped were:
* Tokenization
* POS tagging
* Dependency Parsing
* Named Entity Recognition

The focus of this prototype was on showcasing two different NLP packages, NLTK and spaCy
"""
    )
