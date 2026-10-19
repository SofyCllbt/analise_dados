import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Supermercado",
    layout="centered"
)

st.title("Supermercado")

# Produtos do supermercado
produtos = {
    "Arroz": 20.00,
    "Feijão": 8.00,
    "Leite": 5.00,
    "Pão": 10.00,
    "Café": 15.00
}

# Escolha de vários produtos
produtos_escolhidos = st.multiselect(
    "Escolha os itens do supermercado:",
    list(produtos.keys())
)

# Quantidade de cada produto
total = 0

if produtos_escolhidos:
    st.subheader("Quantidade dos produtos")

    for produto in produtos_escolhidos:
        quantidade = st.number_input(
            f"Quantidade de {produto}",
            min_value=1,
            value=1,
            step=1,
            key=f"qtd_{produto}"
        )

        total += produtos[produto] * quantidade

    st.metric("Preço total da compra", f"R$ {total:.2f}")

else:
    st.info("Escolha pelo menos um produto.")

# Calculadora de troco
st.subheader("Calculadora de Troco")

valor_pago = st.number_input(
    "Valor pago",
    min_value=0.0,
    value=0.0,
    step=1.0
)

if st.button("Calcular Troco", type="primary"):
    if not produtos_escolhidos:
        st.error("Escolha pelo menos um produto.")
    else:
        troco = valor_pago - total

        if troco < 0:
            st.error(
                f"Valor insuficiente. Faltam R$ {abs(troco):.2f}."
            )
        else:
            st.success(f"Troco: R$ {troco:.2f}")