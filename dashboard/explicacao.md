# 📊 Dashboard de Vendas com Streamlit

Este projeto é um dashboard interativo criado com Python e Streamlit para visualizar dados de vendas a partir de um arquivo Excel. Abaixo está uma explicação detalhada de cada parte do código.

[Código completo](main_dashboard.py)

---

## 🧠 Explicação do Código

```python
import streamlit as st  # Ferramenta para criar dashboards e interfaces web em Python
import pandas as pd     # Biblioteca para manipulação e análise de dados
```

**Essas duas bibliotecas são essenciais:**

*streamlit cria a interface visual do dashboard*

*pandas lê e manipula os dados da planilha Excel*

```python
tabela = pd.read_excel("C:/.../vendas.xlsx")  # Lê o arquivo Excel com os dados de vendas
```

Aqui, o código carrega os dados da planilha vendas.xlsx usando o pandas. É importante que o caminho esteja correto e o arquivo contenha colunas como Região, Produto e Valor Venda.

---

```python
st.title("Dashboard de Vendas")  # Define o título principal do dashboard
```

Este comando exibe o título no topo da página do Streamlit.

---

```python
regioes = st.multiselect("Selecione as regiões", tabela["Região"].unique())
```

Cria um campo de seleção múltipla onde o usuário pode escolher uma ou mais regiões.

---

```python
tabela["Região"].unique() # pega todas as regiões disponíveis na base de dados.
```

```python
if regioes:
    tabela = tabela[tabela["Região"].isin(regioes)]
```

Se o usuário selecionar alguma região, o código filtra a tabela para mostrar apenas os dados dessas regiões.

---

```python
st.metric("Faturamento Total", f"R${tabela['Valor Venda'].sum()}")
```

Exibe o faturamento total das vendas filtradas.

---

```python
tabela['Valor Venda'].sum() # calcula a soma de todas as vendas.
```

```python
st.metric("Ticket Médio", f"R${tabela['Valor Venda'].mean()}")
```

Mostra o ticket médio, ou seja, a média do valor das vendas.

---

```python
mean() # calcula a média dos valores.
```

```python
st.bar_chart(tabela.groupby("Região")["Valor Venda"].sum())
```

Gera um gráfico de barras com o faturamento total por região.

---

```python
groupby("Região") #agrupa os dados por região
```

```python
sum() # soma os valores de venda por grupo
```

```python
st.bar_chart(tabela.groupby("Produto")["Valor Venda"].sum())
```

*Cria um gráfico de barras com o faturamento por produto.*

*Assim como o anterior, agrupa por produto e soma os valores.*

---

# 🚀 Como Executar

**Instale as bibliotecas necessárias:**

```bash
pip install streamlit pandas openpyxl
Execute o dashboard:
```

```bash
streamlit run dashboard.py
O navegador abrirá automaticamente com o dashboard interativo.
```
