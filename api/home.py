import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import tweets_downloader as td

def page():
    hash_tag = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    if hash_tag:
        st.write(hash_tag)
        # chamar funcao que conecta com twitter passando como parâmetro "hash_tag"
        #lista = funcao(hash_tag)
        # chamar classificador (modelo) passando a lista dos 10 twitters mais curtidos
        
        pesquisa={hash_tag}
        sentimentos_negativos = {"🤮","🤢","🤬","😡","😠","💩"}
        sentimentos_positivos = {"😍", "🥰", "😋","🤩","😀","😇"}
        queries_positivos = td.create_queries(pesquisa, sentimentos_positivos)
        queries_negativos = td.create_queries(pesquisa, sentimentos_negativos)
        tweets_positivos = td.search(2, queries_positivos); # 50k tweets
        tweets_negativos = td.search(2, queries_negativos); # 50k tweets
        st.write(tweets_positivos)
        st.write(tweets_negativos)
        
