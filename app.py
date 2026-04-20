import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Atualização automática
st.experimental_rerun

sheet_id = "1MCFkO3jnVwjDKHauyq3iXjTfIAdWYe34jDkXN5CoGMw"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

st.set_page_config(page_title="Dashboard de Gestão", layout="wide")

st.title("📊 Perfil de Gestão da Equipe (Ao Vivo)")

# Ler dados
df = pd.read_csv(url)
scores = df.iloc[:, 3].dropna().astype(int)

# Classificação
categorias = {
    "Administrativo": 0,
    "Integrado": 0,
    "Pedagógico": 0
}

for s in scores:
    if s <= 16:
        categorias["Administrativo"] += 1
    elif s <= 23:
        categorias["Integrado"] += 1
    else:
        categorias["Pedagógico"] += 1

col1, col2 = st.columns(2)

with col1:
    st.metric("Total de Respondentes", len(scores))

with col2:
    fig, ax = plt.subplots()
    ax.bar(categorias.keys(), categorias.values())
    ax.set_title("Distribuição dos Perfis")

    for i, v in enumerate(categorias.values()):
        ax.text(i, v, str(v), ha='center', va='bottom')

    st.pyplot(fig)

# Botão de atualização
if st.button("🔄 Atualizar agora"):
    st.rerun()
