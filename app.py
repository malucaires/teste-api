import streamlit as st
from streamlit_option_menu import option_menu
#import home
import analise_comparativa
import analise_exploratoria
#import classificador
import sobre
import tweets_downloader 

#from st_on_hover_tabs import on_hover_tabs
#from src.app import classificador, analise_exploratoria, analise_comparativa, sobre

#st.title("Análise de sentimentos em dados do Twitter")

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home", "Análise exploratória", "Análise comparativa", "Classificador", "Sobre"],
        icons=["house", "search", "book", "folder", "person"],
        menu_icon="cast",
        default_index=0

    )

if selected == "Home":
    #home.page()
    print('ok') #AOAGAR
    #tweets_downloader.page()
    #st.write("Home")
if selected == "Classificador":
    #classificador.page()
    st.write("Classificador")
if selected == "Análise exploratória":
    analise_exploratoria.page()
    st.write("Análise exploratória")
if selected == "Análise comparativa":
    analise_comparativa.page()
    st.write("Análise comparativa")
if selected == "Sobre":
    #sobre.page()
    sobre.teste()

    