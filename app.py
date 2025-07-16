import streamlit as st
import pandas as pd
import plotly.express as px

# Caminho do arquivo CSV
import os
csv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'vehicles.csv')

car_data = pd.read_csv(csv_path)

# Cabeçalho do aplicativo
st.header('Carros')
st.write('Ainda não é um aplicativo funcional. Em construção.')


# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Mensagem de feedback
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criar histograma com Plotly
    fig = px.histogram(car_data, x="odometer")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    # Mensagem de feedback
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # Criar gráfico de dispersão com Plotly
    fig = px.scatter(car_data, x="odometer", y="price")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)
