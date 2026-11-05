import streamlit as st
from main import buscar_jogo

st.set_page_config(page_title="Agente Especialista de Jogos", layout="centered")

st.title("Agente Especialista de Jogos")
st.header("Encontre o jogo ideal para você!")
st.write("Preencha os campos abaixo para receber uma recomendação de jogo com base em suas preferências.")

st.write("")

# Menus suspensos
genero = st.selectbox(
    "Selecione o genero",
    options=["RPG de Aventura", "Corrida", "Tiro"]
)

plataforma = st.selectbox(
    "Selecione a plataforma que você desejar jogar",
    options=["PC", "Console", "Mobile"]
)

hardware = st.selectbox(
    "O jogo deve ser?",
    options=["Leve", "Pesado"]
)

# 1. Definição do Modal (Janela Popup)
@st.dialog("🎮 Recomendação Encontrada!")
def mostrar_modal_jogo(jogo):
    # Conteúdo exibido dentro da janela flutuante
    st.success(f"**Jogo:** {jogo['titulo']}")
    st.write(f"**Gênero:** {jogo['genero']}")
    st.write(f"**Plataforma:** {jogo['plataforma']}")
    st.write(f"**Hardware:** {jogo['hardware']}")
    
    st.divider()
    st.write(f"**Descrição:** {jogo['descricao']}")
    st.caption(f"💡 **Requisitos:** {jogo['specs_resumo']}")
    
    # Botão para fechar o modal
    if st.button("Fechar", type="primary"):
        st.rerun()

# 2. Botão Principal e Disparo do Modal
if st.button("Buscar Jogo"):
    # Busca na main.py
    resultado = buscar_jogo(genero, plataforma, hardware)
    
    if resultado:
        # Chama a função decorada para abrir o Modal na tela
        mostrar_modal_jogo(resultado)
    else:
        st.warning("Nenhum jogo encontrado com os critérios selecionados.")
