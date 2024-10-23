import streamlit as st
import pandas as pd
import altair as alt
st.set_page_config(page_title="Analýza dataset Filmy", page_icon="🎬")
st.title("🎬 Analýza dataset Filmy")
st.write(
    """
    Táto aplikácia vizualizuje údaje z [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    Ukazuje, ktorý filmový žáner mal v kinách za posledné roky najlepší výkon. 
    Stačí kliknúť na miniaplikácie nižšie a preskúmať ich!
    """
)


