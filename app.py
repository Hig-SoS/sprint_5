import streamlit as st
import pandas as pd
import plotly.express as px

# Caminho do arquivo CSV
import os
csv_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'vehicles.csv')

car_data = pd.read_csv(csv_path)

# Cabeçalho do aplicativo
st.title('Cars Sales')

# Exibir tabela com rolagem
st.dataframe(car_data, height=300)

st.header('Odometer')
# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    # Mensagem de feedback
    st.write(
        'Cars volume by odometer')

    # Criar histograma com Plotly
    fig = px.histogram(car_data, x="odometer")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    # Mensagem de feedback
    st.write(
        'Price x Odometer')

    # Criar gráfico de dispersão com Plotly
    fig = px.scatter(car_data, x="odometer", y="price")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Gráficos de relação por Tipo
st.header('Type')

build_histogram = st.checkbox('Show volume of cars by type')

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Volume of cars by type')
    fig = px.histogram(car_data, x="type")
    st.plotly_chart(fig, use_container_width=True)

# Comparações por Tipo
if st.button('Show Type x Condition'):
    st.write('Distribuição de condition para cada type')
    fig = px.histogram(car_data, x="type", color="condition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
elif st.button('Show type x transmitsion'):
    st.write('Distribuição de transmission para cada type')
    fig = px.histogram(car_data, x="type",
                       color="transmission", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
elif st.button('Show type x fuel'):
    st.write('Distribuição de fuel para cada type')
    fig = px.histogram(car_data, x="type", color="fuel", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
