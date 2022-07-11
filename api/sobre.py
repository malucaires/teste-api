import streamlit as st

def page():
    st.title("Sobre")
    st.markdown("## Equipe Lovelace")
    st.markdown("- Gustavo Leitão")
    st.markdown("- José Eliomar")
    st.markdown("- Malu Cairese")
    st.markdown("- Marcos Silva")
    st.markdown("- Paulo Marvin")

def teste():
    h = st.text_input("Pesquisa de HASHTAG", placeholder="Digite uma #hastag")
    st.write(h)