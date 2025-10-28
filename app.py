import streamlit as st
import os

st.set_page_config(page_title="Promoções Cellars", page_icon="🍷", layout="wide")

st.title("🍷 Promoções Cellars")
st.write("Selecione uma categoria para ver as promoções atuais:")

# Dicionário com nomes de pastas e rótulos amigáveis
categorias = {
    "cervejas": "Cervejas",
    "chopps": "Chopps",
    "kits_copos": "Kits e Copos",
    "gourmet": "Gourmet",
    "vinhos_espumantes": "Vinhos / Espumantes",
    "destilados": "Destilados",
    "proximos_vencimento": "Próximos ao Vencimento",
    "novidades_destaques": "Novidades / Destaques"
}

# Sidebar
opcao = st.sidebar.selectbox("Categorias", list(categorias.values()))

# Encontrar a chave correspondente
pasta_categoria = [k for k, v in categorias.items() if v == opcao][0]
caminho_pasta = os.path.join("imagens", pasta_categoria)

# Verificar se há imagens
if not os.path.exists(caminho_pasta) or len(os.listdir(caminho_pasta)) == 0:
    st.warning("🚫 Nenhuma promoção disponível nesta categoria ainda.")
else:
    imagens = [f for f in os.listdir(caminho_pasta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for imagem in imagens:
        caminho_imagem = os.path.join(caminho_pasta, imagem)
        st.image(caminho_imagem, use_container_width=True)
        st.divider()
