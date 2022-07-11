from pandas import DataFrame
import snscrape.modules.twitter as sntwitter
import streamlit as st

def page():

    queries = []
    for restaurante in ['mcdonalds', 'pizza hut']:
        for emoji in ["😍", "🥰", "😋","🤩","😀","😇"]:
            queries.append(f"{restaurante} {emoji}")

    return queries

st.table(page())