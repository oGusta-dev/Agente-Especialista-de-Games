
import streamlit as st 
from main import buscar_jogo

#configaração do titulo da pagina
st.set_page_config(page_title="Agente Especialis", page_icon=":video_game:", layout="centered")

#formulario de busca
st.title("Agente Especialis de Jogos")
st.subheader("Encontre o jogo ideal para você!")
st.text("Preencha os campos abaixo para receber uma recomendação de jogo com base em suas preferências.")
st.write(" ")

genero = st.selectbox(
    "Selecione o genero",
    ["RPG de Aventura","Corrida", "Tiro"]
)
plataforma = st.selectbox(
    "Selecione a plataforma que você desejar jogar",
        ["PC","Console", "Mobile"]
)
hardware = st.selectbox(
    "O jogo deve ser?",
        ["Leve","Pesado"]
)

#realiza a busca do jogo com base nos critérios selecionados
if st.button("Buscar Jogo", type="primary"):
    recomendacao = buscar_jogo(genero, plataforma, hardware)
    if recomendacao:
        st.success(f"Recomendação de Jogo: {recomendacao['titulo']}")
        st.write(f"Gênero: {recomendacao['genero']}")
        st.write(f"Plataforma: {recomendacao['plataforma']}")
        st.write(f"Hardware: {recomendacao['hardware']}")
        st.write(f"Descrição: {recomendacao['descricao']}")
        st.write(f"Especificações Resumidas: {recomendacao['specs_resumo']}")
    else:
        st.error("Nenhum jogo encontrado com os critérios selecionados.")