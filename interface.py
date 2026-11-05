
import streamlit as st 
from main import buscar_jogo

#configaração do titulo da pagina
st.set_page_config(page_title="Agente Especialis", page_icon=":video_game:", layout="centered")

#formulario de busca
st.title("Agente Especialista de Jogos")
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

# Mantém o resultado entre as atualizações da página feitas pelo Streamlit.
if "recomendacao" not in st.session_state:
    st.session_state.recomendacao = None
if "busca_realizada" not in st.session_state:
    st.session_state.busca_realizada = False

col_buscar, col_limpar = st.columns(2)
with col_buscar:
    buscar_clicado = st.button("Buscar Jogo", type="primary")
with col_limpar:
    limpar_clicado = st.button("Limpar pesquisa")

if limpar_clicado:
    st.session_state.recomendacao = None
    st.session_state.busca_realizada = False
elif buscar_clicado:
    st.session_state.recomendacao = buscar_jogo(genero, plataforma, hardware)
    st.session_state.busca_realizada = True

recomendacao = st.session_state.recomendacao
if recomendacao:
    st.success(f"Recomendação de Jogo: {recomendacao['titulo']}")
    col_capa, col_detalhes = st.columns([1, 2])

    with col_capa:
        if recomendacao.get("capa_url"):
            st.image(
                recomendacao["capa_url"],
                caption=recomendacao["titulo"],
                width=220,
                alt=f"Capa do jogo {recomendacao['titulo']}",
            )
        else:
            st.info("Capa não cadastrada para este jogo.")

    with col_detalhes:
        st.write(f"Gênero: {recomendacao['genero']}")
        st.write(f"Plataforma: {recomendacao['plataforma']}")
        st.write(f"Hardware: {recomendacao['hardware']}")
        st.write(f"Descrição: {recomendacao['descricao']}")
        st.write(f"Especificações Resumidas: {recomendacao['specs_resumo']}")
elif st.session_state.busca_realizada:
    st.error("Nenhum jogo encontrado com os critérios selecionados.")
