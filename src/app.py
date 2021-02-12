import streamlit as st
import pandas as pd


def main():
    st.title("TESTE")
    st.dataframe(carrega_dados('dados/obitos-2020.csv'))
    st.text("Texto Teste")  


def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados

if __name__ == '__main__':
    main()