import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import tweets_downloader as td

def page():
    hash_tag = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    if hash_tag:
        st.write(hash_tag)
        lista = [hash_tag]
        tweets = td.search(10, lista); 
        st.write(tweets)

        
