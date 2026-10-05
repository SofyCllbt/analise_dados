import streamlit as st

import pandas as pd

st.write("Olá, mundo")

nome = "Sofia"
idade = 17

st.write("Meu nome é:", nome)
st.write("Minha idade é:", idade)

df = pd.DataFrame({
 "Matérias": ["Português", "Matemática", "Python", "Frame"],
 "Notas": [5, 9, 7, 10]
})

st.title("Meu primeiro dash")

st.subheader(nome)

st.dataframe(df)

produtos = {
 "Arroz": 20.00,
 "Feijão": 8.00,
 "Leite": 5.00,
 "Pão": 10.00,
 "Café": 15.00
}

produto = st.selectbox(
 "Escolha um item do supermercado:",
 list(produtos.keys())
)

def calcular_preco(produto):
 return produtos[produto]

preco = calcular_preco(produto)

st.write("Produto escolhido:", produto)
st.metric("Preço da compra", f"R$ {preco:.2f}")


