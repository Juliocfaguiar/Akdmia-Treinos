import streamlit as st
import pandas as pd
import sqlite3
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf import gerar_pdf

conn = sqlite3.connect('Treinos.db')


cursor = conn.cursor()


# Salva as alterações e fecha a conexão
conn.commit()
conn.close()

col1,col2,col3 = st.columns([1, 1, 1])
with col2:
    st.image("akdmia azul.jpg", width=1000)


col4,col5,col6 = st.columns([0.5, 1, 0.5])
with col5:
    st.title(":blue[Ficha de Treinos]")


def set_individual():
    st.session_state.Individual = True
    st.session_state.Biset = False
    st.session_state.Triset = False

def set_biset():
    st.session_state.Individual = False
    st.session_state.Biset = True
    st.session_state.Triset = False

def set_triset():
    st.session_state.Individual = False
    st.session_state.Biset = False
    st.session_state.Triset = True

col7, col8, col9 = st.columns([1, 1, 1])
with col7:
    st.checkbox(
        "Individual",
        value=st.session_state.get("Individual", False),
        key="Individual",
        on_change=set_individual
    )
with col8:
    st.checkbox(
        "Bi-Set",
        value=st.session_state.get("Biset", False),
        key="Biset",
        on_change=set_biset
    )
with col9:
    st.checkbox(
        "Tri-Set",
        value=st.session_state.get("Triset", False),
        key="Triset",
        on_change=set_triset
    )

quadriceps = ["Agachamento livre", "Agachamento frontal", "Agachamento baixo", "Agachamento alto", "Agachamento no Smith", "Agachamento frontal no Smith", "Agachamento com pausa", "Agachamento búlgaro", "Recuo com halteres", "Avanço com halteres", "Step-up com halteres", "Agachamento búlgaro com halteres", "Agachamento com elevação de calcanhar", "Agachamento sumô", "Leg press 45°", "Leg press 45º com os pés juntos", "Leg press 90°", "Leg press unilateral", "Cadeira extensora", "Cadeira extensora unilateral", "Cadeira extensora com isometria", "Hack machine", "Hack machine reverso", "Smith machine", "Smith machine Frontal", "Agachamento livre", "Agachamento com salto", "Duck walk"]

posteriorCoxa = ["Stiff com barra", "Stiff com halteres", "Stiff unilateral com halteres", "Afundo com halteres", "Terra com pernas rígidas", "Bom dia com barra", "Flexão nórtica", "Mesa flexora", "Cadeira flexora", "Flexora em pé", "Elevação pélvica", "Leg press 45º com os pés altos", "Hack machine com os pés altos"]

peito=["Supino reto com barra", "Supino inclinado com barra", "Supino declinado com barra", "Supino reto com pegada fechada", "Supino reto com halteres", "Supino inclinado com halteres", "Supino declinado com halteres", "Crucifixo reto com halteres", "Crucifixo inclinado com halteres", "Crucifixo declinado com halteres", "Supino com giro", "Pec deck", "peck deck unilateral", "Máquina com pegada neutra", "Cross-over alto", "Cross-over baixo", "Cross-over na linha do peito", "Crucifixo com polia baixa", "Crucifixo com polia alta"]

costas = ["Pulley frente", "Pulley triângulo", "Pulley unilateral", "Remada sentado com triângulo", "Remada sentado com barra", "Remada sentado unilateral", "Remada baixa", "Remada alta", "Remada na máquina Hammer", "Remada na máquina Hammer uni", "Remada curvada com barra", "Remada curvada com halteres", "Remada serrote", "Pulldown com barra", "Pulldown com corda", "Pulldown com triângulo"]

ombros = ["Desenvolvimento frontal com barra", "Elevação frontal com barra", "Desenvolvimento frontal com halteres", "Arnold press", "Elevação frontal com halteres", "Elevação frontal com halteres alternado", "Elevação lateral com halteres", "Elevação lateral com halteres alternado", "Crucifixo invertido com halteres", "Crucifixo invertido com halteres alternado", "Elevação martelo alternada", "Elevação martelo total", "Elevação lateral na polia", "Elevação frontal na polia", "Face pull com corda", "Remada alta na polia baixa", "Crucifixo invertido na máquina peck deck"]

triceps = ["francês unilateral com halteres", "Tríceps kickback com halteres", "Pullover com halteres", "Pulley com barra", "Pulley com corda", "Pulley unilateral com corda", "Pulley inverso com barra", "Pulley inverso com puxador", "Tríceps testa com barra", "Overhead com barra na polia", "Overhead com corda na polia", "Mergulho no banco"]

biceps = ["Rosca direta com barra reta", "Rosca direta com barra W", "Rosca 21", "Rosca no banco Scott", "Rosca no banco Scott alternado", "Rosca alternada com halteres", "Rosca simultânea com halteres", "Rosca martelo com halteres", "Rosca concentrada com halteres", "Rosca cruzada com halteres", "Rosca inclinada total", "Rosca inclinada alternada", "Rosca com corda na polia", "Rosca Zottman", "Rosca inversa com barra", "Rosca inversa com halteres", "Rosca de punho com barra", "Rosca de punho com halteres", "Rosca de punho invertida com halteres"]

series = ["4*8","4*10","4*12","4*15","4*20","4*8~12","5*8","5*10","5*12","5*15","5*20","5*8~12"]


if st.session_state.get("Individual", True):
    st.subheader("Quadríceps",divider="gray")
    col1,col2 = st.columns([1, 0.25])
    with col1:
        primeiro = st.selectbox("Exercício 1", options= quadriceps, key="exercicio1")
    with col2:
        primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series1")
    
    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 2", options=quadriceps, key="exercicio2")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series2")

    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 3", options=quadriceps, key="exercicio3")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series3")

    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 4", options=quadriceps, key="exercicio4")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series4")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    st.subheader("Posterior de Coxa",divider="gray")
    col1,col2 = st.columns([1, 0.25])
    with col1:
        primeiro = st.selectbox("Exercício 1", options= posteriorCoxa, key="exercicio5")
    with col2:
        primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series5")
    
    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 2", options=posteriorCoxa, key="exercicio6")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series6")

    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 3", options=posteriorCoxa, key="exercicio7")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series7")

    col1,col2 = st.columns([1, 0.25])
    with col1:
        segundo = st.selectbox("Exercício 4", options=posteriorCoxa, key="exercicio8")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series8")








# # Botão para gerar e baixar o PDF
# if st.button("Gerar PDF", type="primary", use_container_width=True):
#     if "resultado" in st.session_state and st.session_state.resultado:
#         resultado = st.session_state.resultado               
#         pena_provisoria_pdf = st.session_state.provisorio_pdf if "provisorio" in st.session_state else "Não calculada"            
#         pena_definitiva_pdf = st.session_state.pena_final_com_detração_pdf if "pena_final_com_detração" in st.session_state else "Não calculada"

#         # Gera o PDF
#         pdf_buffer = gerar_pdf(resultado, pena_provisoria_pdf, pena_definitiva_pdf).getvalue()
        
#         # Botão para download do PDF
#         st.download_button(
#             label="Baixar PDF",
#             data=pdf_buffer,
#             file_name="relatorio_sentenca.pdf",
#             mime="application/pdf",
#             key="download_pdf_button"
#         )
#     else:
#         st.error("Por favor, realize o cálculo da pena antes de gerar o PDF.")