import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import tweets_downloader as td
#import data.datacleanning

def page():
    hash_tag = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    if hash_tag:
        st.write(f"Pesquisando tweets com a hashtag {hash_tag}")
        lista = [hash_tag]
        tweets = td.search(500, lista); 
        tweets_ordenados =  sorted(tweets, key=lambda row:row['pontuacao'], reverse=1 )
        st.write(tweets_ordenados)
        
        list_tweets = []
        
        tweets_200 = tweets_ordenados[0:200]
        
        for item in tweets_200:
            valor = item.get('tweet')
            list_tweets.append(valor)
        
        st.table(list_tweets)
        
        