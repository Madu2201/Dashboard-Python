import streamlit as st # Ferramenta de criaçãa de Dashboards e sistemas em Python
import pandas as pd # Que vai gerenciar a base de dados

tabela = pd.read_excel("C:/Users/dudac/OneDrive/Área de Trabalho/Madu/Programação/Visual Studio Code/Dashboard-Python/dashboard/vendas.xlsx") # Lendo arquivo em excel

#print(tabela)

# Titulo do Dashboard
st.title("Dashboard de Vendas") 

# Campo de seleção e filtro dos dados
regioes = st.multiselect("Selecione as regiões", tabela["Região"].unique())

if regioes:
    tabela = tabela[tabela["Região"].isin(regioes)]

# 2 métricas
# faturamento total
st.metric("Faturamento Total", f"R${tabela['Valor Venda'].sum()}")

# ticket médio
st.metric("Ticket Médio", f"R${tabela['Valor Venda'].mean()}")

# gráfico Faturamento por região
st.bar_chart(tabela.groupby("Região")["Valor Venda"].sum())

# gráfico Faturamento por Produto
st.bar_chart(tabela.groupby("Produto")["Valor Venda"].sum())