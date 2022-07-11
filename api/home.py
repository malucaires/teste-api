import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import tweets_downloader

def page():
    hash_tag = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    st.write(hash_tag)
    # chamar funcao que conecta com twitter passando como parâmetro "hash_tag"
    #lista = funcao(hash_tag)
    # chamar classificador (modelo) passando a lista dos 10 twitters mais curtidos
