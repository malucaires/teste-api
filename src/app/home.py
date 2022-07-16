import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import snscrape.modules.twitter as sntwitter
from src.data import tweets_downloader as td
from src.data import data_cleaning_module as dc
import demoji
from joblib import load

def page():
    hash_tag = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    if hash_tag:
        st.write(f"Pesquisando tweets com a hashtag {hash_tag}")
        lista = [hash_tag]
        tweets = td.search(20, lista); 
        tweets_ordenados =  sorted(tweets, key=lambda row:row['pontuacao'], reverse=1 )
      
        tweets_ordenados = pd.DataFrame(tweets_ordenados)
        
        #Remover tweets duplicados
        tweets_ordenados["tweet"] = tweets_ordenados["tweet"].apply(
            lambda tweet: dc.formatar_texto(texto=tweet))
        
        tweets_ordenados["tweet"] = tweets_ordenados["tweet"].apply(
            lambda tweet: dc.remove_special_chars(tweet))
        
        #Remover tweets com menos de 5 palavas
        tweets_ordenados = tweets_ordenados.assign(
            number_words=tweets_ordenados.tweet.apply(lambda x: len(x.split(" "))),
        )  # adiciona coluna com número de palavras
        
        formated_tweets_ordenados = tweets_ordenados.drop(
            tweets_ordenados[tweets_ordenados.number_words < 5].index
        )  # remove tweets com menos de 5 palavras
        
        formated_tweets_ordenados.drop(["number_words"], axis=1, inplace=True)

        #Mostrar os 10 tweets com maior pontuação
        list_tweets = list(formated_tweets_ordenados["tweet"])                         
        list_tweets_10 = list_tweets[0:10]
        st.table(list_tweets_10)
        
        #Préprocessamento de +200
        #Aplicação de funções para remover links, nomes de usuários dos tweets e caracteres especiais.
        formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
            lambda tweet: dc.formatar_texto(texto=tweet))
        formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
            lambda tweet: dc.remove_special_chars(tweet))
        #Remoção dos emojis dos textos
        formated_tweets_ordenados["tweet"] = formated_tweets_ordenados["tweet"].apply(
            lambda tweet: demoji.replace(tweet, "")); # custoso
        
        #Selecionar os 200 tweets com maior pontuação
        list_tweets = list(formated_tweets_ordenados["tweet"])                         
        list_tweets_200 = list_tweets[0:20]
        
        #st.table(list_tweets_200)
        
        preditor = load("src/app/tuned_pipelinev1.joblib") 
        predicao = preditor.predict(list_tweets_200)
        
        predicao[0:5] = 0

        classes = ['negativo', 'positivo']
        fig = plt.figure(figsize=(5, 2))
        plt.barh(
            classes,
            [20, 10]
        )
        plt.xlim([0, 100])
        st.pyplot(fig)
        

        #Gráfico
        
        
       
        #pred_tweet = tuned_pipeline.predict(teste_tweet)
        
        #df_teste = pd.DataFrame(Tweet, pred_tweet),columns=['text','class'])