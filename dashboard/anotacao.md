# 🧰 Guia Prático: Pandas, Streamlit e OpenPyXL

Este documento apresenta uma explicação clara e objetiva sobre três bibliotecas essenciais no ecossistema Python para análise de dados e construção de interfaces: **Pandas**, **Streamlit** e **OpenPyXL**.

---

## 🐼 Pandas

**Pandas** é uma biblioteca poderosa para manipulação e análise de dados estruturados. Ela trabalha principalmente com dois tipos de estruturas: `Series` (vetores) e `DataFrame` (tabelas).

### 🔧 Funcionalidades Principais

- Leitura e escrita de arquivos (CSV, Excel, JSON, SQL)
- Filtros e seleções de dados
- Agrupamentos e agregações
- Estatísticas descritivas
- Manipulação de datas e textos

### 📌 Comandos Essenciais

```python
import pandas as pd
```

# Leitura de arquivos
```python
df = pd.read_csv("dados.csv")
df = pd.read_excel("planilha.xlsx")
```

# Visualização inicia
```python
df.head()           # Mostra as 5 primeiras linhas
df.info()           # Informações gerais
df.describe()       # Estatísticas básicas
```

# Seleção de colunas e linhas
```python
df["coluna"]        # Seleciona uma coluna
df.loc[0]           # Seleciona a primeira linha
df.iloc[0:5]        # Seleciona as 5 primeiras linhas
```

# Filtros
```python
df[df["idade"] > 30]  # Filtra pessoas com idade acima de 30
```

# Agrupamento
```python
df.groupby("categoria")["valor"].sum()
```

# Criação de novas colunas
```python
df["total"] = df["preco"] * df["quantidade"]
```

---

# 🌐 Streamlit

**Streamlit** é uma biblioteca para criação de aplicações web interativas com Python.  
Ideal para dashboards, protótipos e visualizações de dados em tempo real.

---

## 🔧 Funcionalidades Principais

- Interface gráfica com poucos comandos
- Widgets interativos (botões, sliders, seleções)
- Exibição de gráficos e tabelas
- Upload de arquivos
- Atualização dinâmica com base em entrada do usuário

---

## 📌 Comandos Essenciais

```python
import streamlit as st
```

# Título e texto
```python
st.title("Meu Dashboard")
st.subheader("Subtítulo")
st.text("Texto simples")
```

# Widgets
```python
nome = st.text_input("Digite seu nome")
idade = st.slider("Idade", 0, 100)
opcao = st.selectbox("Escolha uma opção", ["A", "B", "C"])
```

# Métricas
```python
st.metric("Vendas", "R$ 10.000", "+5%")
```

# Gráficos
```python
import pandas as pd
df = pd.DataFrame({"Categoria": ["A", "B"], "Valor": [100, 200]})
st.bar_chart(df.set_index("Categoria"))
```

# Upload de arquivos
```python
arquivo = st.file_uploader("Envie um arquivo CSV")
if arquivo:
    dados = pd.read_csv(arquivo)
    st.dataframe(dados)
```

---

# 📄 OpenPyXL

**OpenPyXL** é uma biblioteca para leitura e escrita de arquivos Excel no formato `.xlsx`.  
Ela permite manipular células, estilos, fórmulas e até gráficos diretamente com Python.

---

## 🔧 Funcionalidades Principais

- Leitura e escrita de arquivos `.xlsx`
- Criação de planilhas
- Edição de células e fórmulas
- Estilização (cores, fontes, bordas)
- Inserção de gráficos e imagens

---

## 📌 Comandos Essenciais

```python
from openpyxl import load_workbook, Workbook
```

# Criar nova planilha
```python
wb = Workbook()
ws = wb.active
ws["A1"] = "Nome"
ws["B1"] = "Idade"
ws.append(["Maria", 28])
wb.save("nova_planilha.xlsx")
```

# Ler planilha existente
```python
wb = load_workbook("planilha.xlsx")
ws = wb.active
print(ws["A1"].value)
```

# Estilizar célula
```python
from openpyxl.styles import Font
ws["A1"].font = Font(bold=True, color="FF0000")
wb.save("planilha_estilizada.xlsx")
```

---

# 🔗 Links Úteis

Abaixo estão os links oficiais e recursos recomendados para aprender mais sobre cada biblioteca:

## 🐼 Pandas

- 📘 Documentação oficial: [https://pandas.pydata.org/docs](https://pandas.pydata.org/docs)

---

## 🌐 Streamlit

- 📘 Documentação oficial: [https://docs.streamlit.io](https://docs.streamlit.io)

---

## 📄 OpenPyXL

- 📘 Documentação oficial: [https://openpyxl.readthedocs.io](https://openpyxl.readthedocs.io)

---

## 📦 Instalação das Bibliotecas

Para instalar todas as bibliotecas usadas neste guia:

```bash
pip install pandas streamlit openpyxl
```

