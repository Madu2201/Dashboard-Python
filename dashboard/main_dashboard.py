import streamlit as st
import pandas as pd

tabela = pd.read_excel("vendas.xlsx")

# titulo
st.title("Dashboard de Vendas")

# campo de seleção e filtro dos dados
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