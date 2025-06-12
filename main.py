import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf import gerar_pdf1, gerar_pdf2, gerar_pdf3


col1,col2,col3 = st.columns([1, 1, 1])
with col2:
    st.image("akdmia azul.jpg", width=500)


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



## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

st.checkbox("Quadriceps", value=st.session_state.get("Quadriceps", False), key="Quadriceps")
st.checkbox("Posterior de Coxa", value=st.session_state.get("PosteriorCoxa", False), key="PosteriorCoxa")
st.checkbox("Glúteos", value=st.session_state.get("Gluteos", False), key="Gluteos")
st.checkbox("Peito", value=st.session_state.get("Peito", False), key="Peito")
st.checkbox("Costas", value=st.session_state.get("Costas", False), key="Costas")
st.checkbox("Ombros", value=st.session_state.get("Ombros", False), key="Ombros")
st.checkbox("Tríceps", value=st.session_state.get("Triceps",False), key="Triceps")
st.checkbox("Bíceps", value=st.session_state.get("Biceps", False), key="Biceps")

st.checkbox("Quadriceps + Posterior de Coxa ", value=st.session_state.get("QuadricepsPosteriorCoxa", False), key="QuadricepsPosteriorCoxa")
st.checkbox("Posterior de Coxa + Glúteos", value=st.session_state.get("PosteriorCoxaGluteos", False), key="PosteriorCoxaGluteos")
st.checkbox("Peito + Costas", value=st.session_state.get("PeitoCostas", False), key="PeitoCostas")
st.checkbox("Peito + Ombros", value=st.session_state.get("PeitoOmbros", False), key="PeitoOmbros")
st.checkbox("Peito + Tríceps", value=st.session_state.get("PeitoTriceps", False), key="PeitoTriceps")
st.checkbox("Ombros + Tríceps", value=st.session_state.get("OmbrosTriceps", False), key="OmbrosTriceps")
st.checkbox("Bíceps + Tríceps", value=st.session_state.get("BicepsTriceps", False), key="BicepsTriceps")
st.checkbox("Costas + Bíceps", value=st.session_state.get("CostasBiceps", False), key="CostasBiceps")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##




quadriceps = ["Agachamento livre", "Agachamento frontal", "Agachamento baixo", "Agachamento alto", "Agachamento no Smith", "Agachamento frontal no Smith", "Agachamento com pausa", "Agachamento búlgaro", "Recuo com halteres", "Avanço com halteres", "Step-up com halteres", "Agachamento búlgaro com halteres", "Agachamento com elevação de calcanhar", "Agachamento sumô", "Leg press 45°", "Leg press 45º com os pés juntos", "Leg press 90°", "Leg press unilateral", "Cadeira extensora", "Cadeira extensora unilateral", "Cadeira extensora com isometria", "Hack machine", "Hack machine reverso", "Smith machine", "Smith machine Frontal", "Agachamento livre", "Agachamento com salto", "Duck walk"]

posteriorCoxa = ["Stiff com barra", "Stiff com halteres", "Stiff unilateral com halteres", "Afundo com halteres", "Terra com pernas rígidas", "Bom dia com barra", "Flexão nórtica", "Mesa flexora", "Cadeira flexora", "Flexora em pé", "Elevação pélvica", "Leg press 45º com os pés altos", "Hack machine com os pés altos", "Stiff com barra hexagonal", "Stiff com barra hexagonal unilateral", "Stiff com halteres unilateral", "Stiff com caneleira", "Stiff com caneleira unilateral", "Stiff no banco", "Stiff no banco unilateral", "Stiff no cross", "Stiff no cross unilateral", "Flexão de joelhos no cross", "Flexão de joelhos no cross unilateral"]

gluteos = ["Elevação de quadril com barra", "Elevação de quadril com halteres", "Elevação de quadril com caneleira", "Elevação de quadril no banco", "Elevação de quadril no step", "Elevação de quadril no cross", "Extensão de quadril no cross", "Extensão de quadril com caneleira", "Extensão de quadril em pé", "Extensão de quadril na máquina", "Abdução de quadril em pé", "Abdução de quadril na máquina", "Abdução de quadril com caneleira", "Chute para trás no cross", "Chute lateral no cross", "Chute para trás com caneleira", "Chute lateral com caneleira"]

peito=["Supino reto com barra", "Supino inclinado com barra", "Supino declinado com barra", "Supino reto com pegada fechada", "Supino reto com halteres", "Supino inclinado com halteres", "Supino declinado com halteres", "Crucifixo reto com halteres", "Crucifixo inclinado com halteres", "Crucifixo declinado com halteres", "Supino com giro", "Pec deck", "peck deck unilateral", "Máquina com pegada neutra", "Cross-over alto", "Cross-over baixo", "Cross-over na linha do peito", "Crucifixo com polia baixa", "Crucifixo com polia alta"]

costas = ["Pulley frente", "Pulley triângulo", "Pulley unilateral", "Remada sentado com triângulo", "Remada sentado com barra", "Remada sentado unilateral", "Remada baixa", "Remada alta", "Remada na máquina Hammer", "Remada na máquina Hammer uni", "Remada curvada com barra", "Remada curvada com halteres", "Remada serrote", "Pulldown com barra", "Pulldown com corda", "Pulldown com triângulo","Meio terra"]

ombros = ["Desenvolvimento frontal com barra", "Elevação frontal com barra", "Desenvolvimento frontal com halteres", "Arnold press", "Elevação frontal com halteres", "Elevação frontal com halteres alternado", "Elevação lateral com halteres", "Elevação lateral com halteres alternado", "Crucifixo invertido com halteres", "Crucifixo invertido com halteres alternado", "Elevação martelo alternada", "Elevação martelo total", "Elevação lateral na polia", "Elevação frontal na polia", "Face pull com corda", "Remada alta na polia baixa", "Crucifixo invertido na máquina peck deck"]

triceps = ["francês unilateral com halteres", "Tríceps kickback com halteres", "Pullover com halteres", "Pulley com barra", "Pulley com corda", "Pulley unilateral com corda", "Pulley inverso com barra", "Pulley inverso com puxador", "Tríceps testa com barra", "Overhead com barra na polia", "Overhead com corda na polia", "Mergulho no banco"]

biceps = ["Rosca direta com barra reta", "Rosca direta com barra W", "Rosca 21", "Rosca no banco Scott", "Rosca no banco Scott alternado", "Rosca alternada com halteres", "Rosca simultânea com halteres", "Rosca martelo com halteres", "Rosca concentrada com halteres", "Rosca cruzada com halteres", "Rosca inclinada total", "Rosca inclinada alternada", "Rosca com corda na polia", "Rosca Zottman", "Rosca inversa com barra", "Rosca inversa com halteres", "Rosca de punho com barra", "Rosca de punho com halteres", "Rosca de punho invertida com halteres"]

series = ["4*8","4*10","4*12","4*15","4*20","4*8~12","5*8","5*10","5*12","5*15","5*20","5*8~12","6*8","6*10","6*12","6*15","6*20","6*8~12","7*8","7*10","7*12","7*15","7*20","7*8~12","8*8","8*10","8*12","8*15","8*20","8*8~12","9*8","9*10","9*12","9*15","9*20","9*8~12","10*8","10*10","10*12","10*15","10*20","10*8~12","1*200"]

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

if st.session_state.get("Individual", True):
    if st.session_state.get("Quadriceps", True):
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
    if st.session_state.get("PosteriorCoxa", True):
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

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Peito", True):
        st.subheader("Peito",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito, key="exercicio9")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series9")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito, key="exercicio10")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series10")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito, key="exercicio11")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series11")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito, key="exercicio12")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series12")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Costas", True):
        st.subheader("Costas",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= costas, key="exercicio13")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series13")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=costas, key="exercicio14")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series14")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=costas, key="exercicio15")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series15")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=costas, key="exercicio16")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series16")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Ombros", True):
        st.subheader("Ombros",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= ombros, key="exercicio17")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series17")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=ombros, key="exercicio18")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series18")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=ombros, key="exercicio19")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series19")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=ombros, key="exercicio20")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series20")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Triceps", True):
        st.subheader("Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= triceps, key="exercicio21")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series21")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=triceps, key="exercicio22")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series22")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=triceps, key="exercicio23")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series23")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=triceps, key="exercicio24")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series24")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Biceps", True):
        st.subheader("Bíceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= biceps, key="exercicio25")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series25")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=biceps, key="exercicio26")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series26")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=biceps, key="exercicio27")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series27")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=biceps, key="exercicio28")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series28")

    ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Gluteos", True):
        st.subheader("Glúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= gluteos, key="exercicio29")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series29")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=gluteos, key="exercicio30")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series30")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=gluteos, key="exercicio31")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series31")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=gluteos, key="exercicio32")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series32")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("QuadricepsPosteriorCoxa", True):
        st.subheader("Quadríceps + Posterior de Coxa",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= quadriceps+posteriorCoxa, key="exercicio33")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series33")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=quadriceps+posteriorCoxa, key="exercicio34")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series34")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=quadriceps+posteriorCoxa, key="exercicio35")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series35")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=quadriceps+posteriorCoxa, key="exercicio36")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series36")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PosteriorCoxaGluteos", True):
        st.subheader("Posterior de Coxa + Glúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= posteriorCoxa+gluteos, key="exercicio37")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series37")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=posteriorCoxa+gluteos, key="exercicio38")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series38")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=posteriorCoxa+gluteos, key="exercicio39")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series39")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=posteriorCoxa+gluteos, key="exercicio40")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series40")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PeitoCostas", True):
        st.subheader("Peito + Costas",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito+costas, key="exercicio41")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series41")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito+costas, key="exercicio42")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series42")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito+costas, key="exercicio43")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series43")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito+costas, key="exercicio44")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series44")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PeitoOmbros", True):
        st.subheader("Peito + Ombros",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito+ombros, key="exercicio45")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series45")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito+ombros, key="exercicio46")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series46")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito+ombros, key="exercicio47")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series47")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito+ombros, key="exercicio48")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series48")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PeitoTriceps", True):
        st.subheader("Peito + Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito+triceps, key="exercicio49")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series49")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito+triceps, key="exercicio50")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series50")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito+triceps, key="exercicio51")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series51")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito+triceps, key="exercicio52")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series52")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("OmbrosTriceps", True):
        st.subheader("Ombros + Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= ombros+triceps, key="exercicio53")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series53")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=ombros+triceps, key="exercicio54")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series54")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=ombros+triceps, key="exercicio55")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series55")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=ombros+triceps, key="exercicio56")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series56")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("BicepsTriceps", True):
        st.subheader("Bíceps + Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= biceps+triceps, key="exercicio57")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series57")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=biceps+triceps, key="exercicio58")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series58")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=biceps+triceps, key="exercicio59")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series59")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=biceps+triceps, key="exercicio60")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series60")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("CostasBiceps", True):
        st.subheader("Costas + Bíceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= costas+biceps, key="exercicio61")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series61")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=costas+biceps, key="exercicio62")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series62")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=costas+biceps, key="exercicio63")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series63")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=costas+biceps, key="exercicio64")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series64")
       
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


    dados_treino1 = {
        "exercicio1": st.session_state.get("exercicio1"),
        "series1": st.session_state.get("series1"),
        "exercicio2": st.session_state.get("exercicio2"),
        "series2": st.session_state.get("series2"),
        "exercicio3": st.session_state.get("exercicio3"),
        "series3": st.session_state.get("series3"),
        "exercicio4": st.session_state.get("exercicio4"),
        "series4": st.session_state.get("series4"),
        "exercicio5": st.session_state.get("exercicio5"),
        "series5": st.session_state.get("series5"),
        "exercicio6": st.session_state.get("exercicio6"),
        "series6": st.session_state.get("series6"),
        "exercicio7": st.session_state.get("exercicio7"),
        "series7": st.session_state.get("series7"),
        "exercicio8": st.session_state.get("exercicio8"),
        "series8": st.session_state.get("series8"),
        "exercicio9": st.session_state.get("exercicio9"),
        "series9": st.session_state.get("series9"),
        "exercicio10": st.session_state.get("exercicio10"),
        "series10": st.session_state.get("series10"),
        "exercicio11": st.session_state.get("exercicio11"),
        "series11": st.session_state.get("series11"),
        "exercicio12": st.session_state.get("exercicio12"),
        "series12": st.session_state.get("series12"),
        "exercicio13": st.session_state.get("exercicio13"),
        "series13": st.session_state.get("series13"),
        "exercicio14": st.session_state.get("exercicio14"),
        "series14": st.session_state.get("series14"),
        "exercicio15": st.session_state.get("exercicio15"),
        "series15": st.session_state.get("series15"),
        "exercicio16": st.session_state.get("exercicio16"),
        "series16": st.session_state.get("series16"),
        "exercicio17": st.session_state.get("exercicio17"),
        "series17": st.session_state.get("series17"),
        "exercicio18": st.session_state.get("exercicio18"),
        "series18": st.session_state.get("series18"),
        "exercicio19": st.session_state.get("exercicio19"),
        "series19": st.session_state.get("series19"),
        "exercicio20": st.session_state.get("exercicio20"),
        "series20": st.session_state.get("series20"),
        "exercicio21": st.session_state.get("exercicio21"),
        "series21": st.session_state.get("series21"),
        "exercicio22": st.session_state.get("exercicio22"),
        "series22": st.session_state.get("series22"),
        "exercicio23": st.session_state.get("exercicio23"),
        "series23": st.session_state.get("series23"),
        "exercicio24": st.session_state.get("exercicio24"),
        "series24": st.session_state.get("series24"),
        "exercicio25": st.session_state.get("exercicio25"),
        "series25": st.session_state.get("series25"),
        "exercicio26": st.session_state.get("exercicio26"),
        "series26": st.session_state.get("series26"),
        "exercicio27": st.session_state.get("exercicio27"),
        "series27": st.session_state.get("series27"),
        "exercicio28": st.session_state.get("exercicio28"),
        "series28": st.session_state.get("series28"),
        "exercicio29": st.session_state.get("exercicio29"),
        "series29": st.session_state.get("series29"),
        "exercicio30": st.session_state.get("exercicio30"),
        "series30": st.session_state.get("series30"),
        "exercicio31": st.session_state.get("exercicio31"),
        "series31": st.session_state.get("series31"),
        "exercicio32": st.session_state.get("exercicio32"),
        "series32": st.session_state.get("series32"),
        "exercicio33": st.session_state.get("exercicio33"),
        "series33": st.session_state.get("series33"),
        "exercicio34": st.session_state.get("exercicio34"),
        "series34": st.session_state.get("series34"),
        "exercicio35": st.session_state.get("exercicio35"),
        "series35": st.session_state.get("series35"),
        "exercicio36": st.session_state.get("exercicio36"),
        "series36": st.session_state.get("series36"),
        "exercicio37": st.session_state.get("exercicio37"),
        "series37": st.session_state.get("series37"),
        "exercicio38": st.session_state.get("exercicio38"),
        "series38": st.session_state.get("series38"),
        "exercicio39": st.session_state.get("exercicio39"),
        "series39": st.session_state.get("series39"),
        "exercicio40": st.session_state.get("exercicio40"),
        "series40": st.session_state.get("series40"),
        "exercicio41": st.session_state.get("exercicio41"),
        "series41": st.session_state.get("series41"),
        "exercicio42": st.session_state.get("exercicio42"),
        "series42": st.session_state.get("series42"),
        "exercicio43": st.session_state.get("exercicio43"),
        "series43": st.session_state.get("series43"),
        "exercicio44": st.session_state.get("exercicio44"),
        "series44": st.session_state.get("series44"),
        "exercicio45": st.session_state.get("exercicio45"),
        "series45": st.session_state.get("series45"),
        "exercicio46": st.session_state.get("exercicio46"),
        "series46": st.session_state.get("series46"),
        "exercicio47": st.session_state.get("exercicio47"),
        "series47": st.session_state.get("series47"),
        "exercicio48": st.session_state.get("exercicio48"),
        "series48": st.session_state.get("series48"),
        "exercicio49": st.session_state.get("exercicio49"),
        "series49": st.session_state.get("series49"),
        "exercicio50": st.session_state.get("exercicio50"),
        "series50": st.session_state.get("series50"),
        "exercicio51": st.session_state.get("exercicio51"),
        "series51": st.session_state.get("series51"),
        "exercicio52": st.session_state.get("exercicio52"),
        "series52": st.session_state.get("series52"),
        "exercicio53": st.session_state.get("exercicio53"),
        "series53": st.session_state.get("series53"),
        "exercicio54": st.session_state.get("exercicio54"),
        "series54": st.session_state.get("series54"),
        "exercicio55": st.session_state.get("exercicio55"),
        "series55": st.session_state.get("series55"),
        "exercicio56": st.session_state.get("exercicio56"),
        "series56": st.session_state.get("series56"),
        "exercicio57": st.session_state.get("exercicio57"),
        "series57": st.session_state.get("series57"),
        "exercicio58": st.session_state.get("exercicio58"),
        "series58": st.session_state.get("series58"),
        "exercicio59": st.session_state.get("exercicio59"),
        "series59": st.session_state.get("series59"),
        "exercicio60": st.session_state.get("exercicio60"),
        "series60": st.session_state.get("series60"),
        "exercicio61": st.session_state.get("exercicio61"),
        "series61": st.session_state.get("series61"),
        "exercicio62": st.session_state.get("exercicio62"),
        "series62": st.session_state.get("series62"),
        "exercicio63": st.session_state.get("exercicio63"),
        "series63": st.session_state.get("series63"),
        "exercicio64": st.session_state.get("exercicio64"),
        "series64": st.session_state.get("series64"),

    }
    st.session_state["dados_treino"] = dados_treino1

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

    if st.session_state.get("Quadriceps", True) or \
        st.session_state.get("PosteriorCoxa", True) or \
        st.session_state.get("Peito", True) or \
        st.session_state.get("Costas", True) or \
        st.session_state.get("Ombros", True) or \
        st.session_state.get("Triceps", True) or \
        st.session_state.get("Biceps", True) or \
        st.session_state.get("Gluteos", True) or \
        st.session_state.get("QuadricepsPosteriorCoxa", True) or \
        st.session_state.get("PosteriorCoxaGluteos", True) or \
        st.session_state.get("PeitoCostas", True) or \
        st.session_state.get("PeitoOmbros", True) or \
        st.session_state.get("PeitoTriceps", True) or \
        st.session_state.get("OmbrosTriceps", True) or \
        st.session_state.get("BicepsTriceps", True) or \
        st.session_state.get("CostasBiceps", True):
        # Botão para gerar PDF
        if st.button("Gerar PDF"):
            from pdf import gerar_pdf1
            gerar_pdf1(st.session_state["dados_treino"])


        pdf_buffer1 = gerar_pdf1(dados_treino1).getvalue()

        #  Botão para download do PDF

        st.download_button(
            label="Baixar PDF",
            data=pdf_buffer1,
            file_name="FichaTreino.pdf",
            mime="pdf",
            key="download_pdf_button"
                )
    
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##



## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

if st.session_state.get("Biset", True):
    if st.session_state.get("Quadriceps", True):
        st.subheader("Quadríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= quadriceps, key="exercicio1")
            primeiro = st.selectbox("", options= quadriceps, key="exercicio01")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series1")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=quadriceps, key="exercicio2")
            segundo = st.selectbox("", options=quadriceps, key="exercicio02")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series2")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=quadriceps, key="exercicio3")
            segundo = st.selectbox("", options=quadriceps, key="exercicio03")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series3")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=quadriceps, key="exercicio4")
            segundo = st.selectbox("", options=quadriceps, key="exercicio04")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series4")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PosteriorCoxa", True):
        st.subheader("Posterior de Coxa + Clúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= posteriorCoxa, key="exercicio5")
            primeiro = st.selectbox("", options= posteriorCoxa, key="exercicio05")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series5")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=posteriorCoxa, key="exercicio6")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio06")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series6")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=posteriorCoxa, key="exercicio7")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio07")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series7")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=posteriorCoxa, key="exercicio8")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio08")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series8")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Peito", True):
        st.subheader("Peito",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito, key="exercicio9")
            primeiro = st.selectbox("", options= peito, key="exercicio09")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series9")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito, key="exercicio10")
            segundo = st.selectbox("", options=peito, key="exercicio010")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series10")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito, key="exercicio11")
            segundo = st.selectbox("", options=peito, key="exercicio011")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series11")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito, key="exercicio12")
            segundo = st.selectbox("", options=peito, key="exercicio012")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series12")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Costas", True):
        st.subheader("Costas",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= costas, key="exercicio13")
            primeiro = st.selectbox("", options= costas, key="exercicio013")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series13")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=costas, key="exercicio14")
            segundo = st.selectbox("", options=costas, key="exercicio014")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series14")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=costas, key="exercicio15")
            segundo = st.selectbox("", options=costas, key="exercicio015")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series15")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=costas, key="exercicio16")
            segundo = st.selectbox("", options=costas, key="exercicio016")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series16")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Ombros", True):
        st.subheader("Ombros",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= ombros, key="exercicio17")
            primeiro = st.selectbox("", options= ombros, key="exercicio017")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series17")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=ombros, key="exercicio18")
            segundo = st.selectbox("", options=ombros, key="exercicio018")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series18")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=ombros, key="exercicio19")
            segundo = st.selectbox("", options=ombros, key="exercicio019")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series19")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=ombros, key="exercicio20")
            segundo = st.selectbox("", options=ombros, key="exercicio020")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series20")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Triceps", True):
        st.subheader("Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= triceps, key="exercicio21")
            primeiro = st.selectbox("", options= triceps, key="exercicio021")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series21")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=triceps, key="exercicio22")
            segundo = st.selectbox("", options=triceps, key="exercicio022")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series22")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=triceps, key="exercicio23")
            segundo = st.selectbox("", options=triceps, key="exercicio023")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series23")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=triceps, key="exercicio24")
            segundo = st.selectbox("", options=triceps, key="exercicio024")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series24")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Biceps", True):
        st.subheader("Bíceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= biceps, key="exercicio25")
            primeiro = st.selectbox("", options= biceps, key="exercicio025")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series25")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=biceps, key="exercicio26")
            segundo = st.selectbox("", options=biceps, key="exercicio026")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series26")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=biceps, key="exercicio27")
            segundo = st.selectbox("", options=biceps, key="exercicio027")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series27")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=biceps, key="exercicio28")
            segundo = st.selectbox("", options=biceps, key="exercicio028")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series28")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Gluteos", True):
        st.subheader("Glúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= gluteos, key="exercicio29")
            primeiro = st.selectbox("", options= gluteos, key="exercicio029")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series29")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=gluteos, key="exercicio30")
            segundo = st.selectbox("", options=gluteos, key="exercicio030")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series30")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=gluteos, key="exercicio31")
            segundo = st.selectbox("", options=gluteos, key="exercicio031")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series31")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=gluteos, key="exercicio32")
            segundo = st.selectbox("", options=gluteos, key="exercicio032")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series32")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


    dados_treino2 = {
        "exercicio1": st.session_state.get("exercicio1"),
        "series1": st.session_state.get("series1"),
        "exercicio2": st.session_state.get("exercicio2"),
        "series2": st.session_state.get("series2"),
        "exercicio3": st.session_state.get("exercicio3"),
        "series3": st.session_state.get("series3"),
        "exercicio4": st.session_state.get("exercicio4"),
        "series4": st.session_state.get("series4"),
        "exercicio5": st.session_state.get("exercicio5"),
        "series5": st.session_state.get("series5"),
        "exercicio6": st.session_state.get("exercicio6"),
        "series6": st.session_state.get("series6"),
        "exercicio7": st.session_state.get("exercicio7"),
        "series7": st.session_state.get("series7"),
        "exercicio8": st.session_state.get("exercicio8"),
        "series8": st.session_state.get("series8"),
        "exercicio9": st.session_state.get("exercicio9"),
        "series9": st.session_state.get("series9"),
        "exercicio10": st.session_state.get("exercicio10"),
        "series10": st.session_state.get("series10"),
        "exercicio11": st.session_state.get("exercicio11"),
        "series11": st.session_state.get("series11"),
        "exercicio12": st.session_state.get("exercicio12"),
        "series12": st.session_state.get("series12"),
        "exercicio13": st.session_state.get("exercicio13"),
        "series13": st.session_state.get("series13"),
        "exercicio14": st.session_state.get("exercicio14"),
        "series14": st.session_state.get("series14"),
        "exercicio15": st.session_state.get("exercicio15"),
        "series15": st.session_state.get("series15"),
        "exercicio16": st.session_state.get("exercicio16"),
        "series16": st.session_state.get("series16"),
        "exercicio17": st.session_state.get("exercicio17"),
        "series17": st.session_state.get("series17"),
        "exercicio18": st.session_state.get("exercicio18"),
        "series18": st.session_state.get("series18"),
        "exercicio19": st.session_state.get("exercicio19"),
        "series19": st.session_state.get("series19"),
        "exercicio20": st.session_state.get("exercicio20"),
        "series20": st.session_state.get("series20"),
        "exercicio21": st.session_state.get("exercicio21"),
        "series21": st.session_state.get("series21"),
        "exercicio22": st.session_state.get("exercicio22"),
        "series22": st.session_state.get("series22"),
        "exercicio23": st.session_state.get("exercicio23"),
        "series23": st.session_state.get("series23"),
        "exercicio24": st.session_state.get("exercicio24"),
        "series24": st.session_state.get("series24"),
        "exercicio25": st.session_state.get("exercicio25"),
        "series25": st.session_state.get("series25"),
        "exercicio26": st.session_state.get("exercicio26"),
        "series26": st.session_state.get("series26"),
        "exercicio27": st.session_state.get("exercicio27"),
        "series27": st.session_state.get("series27"),
        "exercicio28": st.session_state.get("exercicio28"),
        "series28": st.session_state.get("series28"),
        "exercicio29": st.session_state.get("exercicio29"),
        "series29": st.session_state.get("series29"),
        "exercicio30": st.session_state.get("exercicio30"),
        "series30": st.session_state.get("series30"),
        "exercicio31": st.session_state.get("exercicio31"),
        "series31": st.session_state.get("series31"),
        "exercicio32": st.session_state.get("exercicio32"),
        "series32": st.session_state.get("series32"),

        "exercicio01": st.session_state.get("exercicio01"),
        "exercicio02": st.session_state.get("exercicio02"),
        "exercicio03": st.session_state.get("exercicio03"),
        "exercicio04": st.session_state.get("exercicio04"),
        "exercicio05": st.session_state.get("exercicio05"),
        "exercicio06": st.session_state.get("exercicio06"),
        "exercicio07": st.session_state.get("exercicio07"),
        "exercicio08": st.session_state.get("exercicio08"),
        "exercicio09": st.session_state.get("exercicio09"),
        "exercicio010": st.session_state.get("exercicio010"),
        "exercicio011": st.session_state.get("exercicio011"),
        "exercicio012": st.session_state.get("exercicio012"),
        "exercicio013": st.session_state.get("exercicio013"),
        "exercicio014": st.session_state.get("exercicio014"),
        "exercicio015": st.session_state.get("exercicio015"),
        "exercicio016": st.session_state.get("exercicio016"),
        "exercicio017": st.session_state.get("exercicio017"),
        "exercicio018": st.session_state.get("exercicio018"),
        "exercicio019": st.session_state.get("exercicio019"),
        "exercicio020": st.session_state.get("exercicio020"),
        "exercicio021": st.session_state.get("exercicio021"),
        "exercicio022": st.session_state.get("exercicio022"),
        "exercicio023": st.session_state.get("exercicio023"),
        "exercicio024": st.session_state.get("exercicio024"),
        "exercicio025": st.session_state.get("exercicio025"),
        "exercicio026": st.session_state.get("exercicio026"),
        "exercicio027": st.session_state.get("exercicio027"),
        "exercicio028": st.session_state.get("exercicio028"),
        "exercicio029": st.session_state.get("exercicio029"),
        "exercicio030": st.session_state.get("exercicio030"),
        "exercicio031": st.session_state.get("exercicio031"),
        "exercicio032": st.session_state.get("exercicio032"),
    }
    st.session_state["dados_treino"] = dados_treino2

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

    if st.session_state.get("Quadriceps", True) or \
        st.session_state.get("PosteriorCoxa", True) or \
        st.session_state.get("Peito", True) or \
        st.session_state.get("Costas", True) or \
        st.session_state.get("Ombros", True) or \
        st.session_state.get("Triceps", True) or \
        st.session_state.get("Biceps", True) or \
        st.session_state.get("Gluteos", True):
        # Botão para gerar PDF
        if st.button("Gerar PDF"):
            from pdf import gerar_pdf2
            gerar_pdf2(st.session_state["dados_treino"])


        pdf_buffer2 = gerar_pdf2(dados_treino2).getvalue()

        #  Botão para download do PDF

        st.download_button(
            label="Baixar PDF",
            data=pdf_buffer2,
            file_name="FichaTreino.pdf",
            mime="pdf",
            key="download_pdf_button"
                )
    
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##



## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

if st.session_state.get("Triset", True):
    if st.session_state.get("Quadriceps", True):
        st.subheader("Quadríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= quadriceps, key="exercicio1")
            primeiro = st.selectbox("", options= quadriceps, key="exercicio01")
            primeiro = st.selectbox("", options= quadriceps, key="exercicio001")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series1")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=quadriceps, key="exercicio2")
            segundo = st.selectbox("", options=quadriceps, key="exercicio02")
            segundo = st.selectbox("", options=quadriceps, key="exercicio002")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series2")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=quadriceps, key="exercicio3")
            segundo = st.selectbox("", options=quadriceps, key="exercicio03")
            segundo = st.selectbox("", options=quadriceps, key="exercicio003")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series3")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=quadriceps, key="exercicio4")
            segundo = st.selectbox("", options=quadriceps, key="exercicio04")
            segundo = st.selectbox("", options=quadriceps, key="exercicio004")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series4")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("PosteriorCoxa", True):
        st.subheader("Posterior de Coxa + Clúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= posteriorCoxa, key="exercicio5")
            primeiro = st.selectbox("", options= posteriorCoxa, key="exercicio05")
            primeiro = st.selectbox("", options= posteriorCoxa, key="exercicio005")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series5")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=posteriorCoxa, key="exercicio6")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio06")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio006")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series6")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=posteriorCoxa, key="exercicio7")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio07")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio007")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series7")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=posteriorCoxa, key="exercicio8")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio08")
            segundo = st.selectbox("", options=posteriorCoxa, key="exercicio008")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series8")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Peito", True):
        st.subheader("Peito",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= peito, key="exercicio9")
            primeiro = st.selectbox("", options= peito, key="exercicio09")
            primeiro = st.selectbox("", options= peito, key="exercicio009")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series9")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=peito, key="exercicio10")
            segundo = st.selectbox("", options=peito, key="exercicio010")
            segundo = st.selectbox("", options=peito, key="exercicio0010")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series10")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=peito, key="exercicio11")
            segundo = st.selectbox("", options=peito, key="exercicio011")
            segundo = st.selectbox("", options=peito, key="exercicio0011")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series11")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=peito, key="exercicio12")
            segundo = st.selectbox("", options=peito, key="exercicio012")
            segundo = st.selectbox("", options=peito, key="exercicio0012")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series12")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Costas", True):
        st.subheader("Costas",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= costas, key="exercicio13")
            primeiro = st.selectbox("", options= costas, key="exercicio013")
            primeiro = st.selectbox("", options= costas, key="exercicio0013")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series13")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=costas, key="exercicio14")
            segundo = st.selectbox("", options=costas, key="exercicio014")
            segundo = st.selectbox("", options=costas, key="exercicio0014")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series14")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=costas, key="exercicio15")
            segundo = st.selectbox("", options=costas, key="exercicio015")
            segundo = st.selectbox("", options=costas, key="exercicio0015")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series15")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=costas, key="exercicio16")
            segundo = st.selectbox("", options=costas, key="exercicio016")
            segundo = st.selectbox("", options=costas, key="exercicio0016")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series16")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Ombros", True):
        st.subheader("Ombros",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= ombros, key="exercicio17")
            primeiro = st.selectbox("", options= ombros, key="exercicio017")
            primeiro = st.selectbox("", options= ombros, key="exercicio0017")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series17")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=ombros, key="exercicio18")
            segundo = st.selectbox("", options=ombros, key="exercicio018")
            segundo = st.selectbox("", options=ombros, key="exercicio0018")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series18")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=ombros, key="exercicio19")
            segundo = st.selectbox("", options=ombros, key="exercicio019")
            segundo = st.selectbox("", options=ombros, key="exercicio0019")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series19")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=ombros, key="exercicio20")
            segundo = st.selectbox("", options=ombros, key="exercicio020")
            segundo = st.selectbox("", options=ombros, key="exercicio0020")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series20")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Triceps", True):
        st.subheader("Tríceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= triceps, key="exercicio21")
            primeiro = st.selectbox("", options= triceps, key="exercicio021")
            primeiro = st.selectbox("", options= triceps, key="exercicio0021")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series21")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=triceps, key="exercicio22")
            segundo = st.selectbox("", options=triceps, key="exercicio022")
            segundo = st.selectbox("", options=triceps, key="exercicio0022")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series22")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=triceps, key="exercicio23")
            segundo = st.selectbox("", options=triceps, key="exercicio023")
            segundo = st.selectbox("", options=triceps, key="exercicio0023")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series23")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=triceps, key="exercicio24")
            segundo = st.selectbox("", options=triceps, key="exercicio024")
            segundo = st.selectbox("", options=triceps, key="exercicio0024")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series24")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Biceps", True):
        st.subheader("Bíceps",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= biceps, key="exercicio25")
            primeiro = st.selectbox("", options= biceps, key="exercicio025")
            primeiro = st.selectbox("", options= biceps, key="exercicio0025")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series25")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=biceps, key="exercicio26")
            segundo = st.selectbox("", options=biceps, key="exercicio026")
            segundo = st.selectbox("", options=biceps, key="exercicio0026")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series26")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=biceps, key="exercicio27")
            segundo = st.selectbox("", options=biceps, key="exercicio027")
            segundo = st.selectbox("", options=biceps, key="exercicio0027")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series27")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=biceps, key="exercicio28")
            segundo = st.selectbox("", options=biceps, key="exercicio028")
            segundo = st.selectbox("", options=biceps, key="exercicio0028")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series28")
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
    if st.session_state.get("Gluteos", True):
        st.subheader("Glúteos",divider="gray")
        col1,col2 = st.columns([1, 0.25])
        with col1:
            primeiro = st.selectbox("Exercício 1", options= gluteos, key="exercicio29")
            primeiro = st.selectbox("", options= gluteos, key="exercicio029")
            primeiro = st.selectbox("", options= gluteos, key="exercicio0029")
        with col2:
            primeiro_series = st.selectbox("Séries/Repetições", options=series, key="series29")
        
        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 2", options=gluteos, key="exercicio30")
            segundo = st.selectbox("", options=gluteos, key="exercicio030")
            segundo = st.selectbox("", options=gluteos, key="exercicio0030")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series30")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 3", options=gluteos, key="exercicio31")
            segundo = st.selectbox("", options=gluteos, key="exercicio031")
            segundo = st.selectbox("", options=gluteos, key="exercicio0031")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series31")

        col1,col2 = st.columns([1, 0.25])
        with col1:
            segundo = st.selectbox("Exercício 4", options=gluteos, key="exercicio32")
            segundo = st.selectbox("", options=gluteos, key="exercicio032")
            segundo = st.selectbox("", options=gluteos, key="exercicio0032")
        with col2:
            segundo_series = st.selectbox("Séries/Repetições", options=series, key="series32")


## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


    dados_treino3 = {
        "exercicio1": st.session_state.get("exercicio1"),
        "series1": st.session_state.get("series1"),
        "exercicio2": st.session_state.get("exercicio2"),
        "series2": st.session_state.get("series2"),
        "exercicio3": st.session_state.get("exercicio3"),
        "series3": st.session_state.get("series3"),
        "exercicio4": st.session_state.get("exercicio4"),
        "series4": st.session_state.get("series4"),
        "exercicio5": st.session_state.get("exercicio5"),
        "series5": st.session_state.get("series5"),
        "exercicio6": st.session_state.get("exercicio6"),
        "series6": st.session_state.get("series6"),
        "exercicio7": st.session_state.get("exercicio7"),
        "series7": st.session_state.get("series7"),
        "exercicio8": st.session_state.get("exercicio8"),
        "series8": st.session_state.get("series8"),
        "exercicio9": st.session_state.get("exercicio9"),
        "series9": st.session_state.get("series9"),
        "exercicio10": st.session_state.get("exercicio10"),
        "series10": st.session_state.get("series10"),
        "exercicio11": st.session_state.get("exercicio11"),
        "series11": st.session_state.get("series11"),
        "exercicio12": st.session_state.get("exercicio12"),
        "series12": st.session_state.get("series12"),
        "exercicio13": st.session_state.get("exercicio13"),
        "series13": st.session_state.get("series13"),
        "exercicio14": st.session_state.get("exercicio14"),
        "series14": st.session_state.get("series14"),
        "exercicio15": st.session_state.get("exercicio15"),
        "series15": st.session_state.get("series15"),
        "exercicio16": st.session_state.get("exercicio16"),
        "series16": st.session_state.get("series16"),
        "exercicio17": st.session_state.get("exercicio17"),
        "series17": st.session_state.get("series17"),
        "exercicio18": st.session_state.get("exercicio18"),
        "series18": st.session_state.get("series18"),
        "exercicio19": st.session_state.get("exercicio19"),
        "series19": st.session_state.get("series19"),
        "exercicio20": st.session_state.get("exercicio20"),
        "series20": st.session_state.get("series20"),
        "exercicio21": st.session_state.get("exercicio21"),
        "series21": st.session_state.get("series21"),
        "exercicio22": st.session_state.get("exercicio22"),
        "series22": st.session_state.get("series22"),
        "exercicio23": st.session_state.get("exercicio23"),
        "series23": st.session_state.get("series23"),
        "exercicio24": st.session_state.get("exercicio24"),
        "series24": st.session_state.get("series24"),
        "exercicio25": st.session_state.get("exercicio25"),
        "series25": st.session_state.get("series25"),
        "exercicio26": st.session_state.get("exercicio26"),
        "series26": st.session_state.get("series26"),
        "exercicio27": st.session_state.get("exercicio27"),
        "series27": st.session_state.get("series27"),
        "exercicio28": st.session_state.get("exercicio28"),
        "series28": st.session_state.get("series28"),
        "exercicio29": st.session_state.get("exercicio29"),
        "series29": st.session_state.get("series29"),
        "exercicio30": st.session_state.get("exercicio30"),
        "series30": st.session_state.get("series30"),
        "exercicio31": st.session_state.get("exercicio31"),
        "series31": st.session_state.get("series31"),
        "exercicio32": st.session_state.get("exercicio32"),
        "series32": st.session_state.get("series32"),

        "exercicio01": st.session_state.get("exercicio01"),
        "exercicio02": st.session_state.get("exercicio02"),
        "exercicio03": st.session_state.get("exercicio03"),
        "exercicio04": st.session_state.get("exercicio04"),
        "exercicio05": st.session_state.get("exercicio05"),
        "exercicio06": st.session_state.get("exercicio06"),
        "exercicio07": st.session_state.get("exercicio07"),
        "exercicio08": st.session_state.get("exercicio08"),
        "exercicio09": st.session_state.get("exercicio09"),
        "exercicio010": st.session_state.get("exercicio010"),
        "exercicio011": st.session_state.get("exercicio011"),
        "exercicio012": st.session_state.get("exercicio012"),
        "exercicio013": st.session_state.get("exercicio013"),
        "exercicio014": st.session_state.get("exercicio014"),
        "exercicio015": st.session_state.get("exercicio015"),
        "exercicio016": st.session_state.get("exercicio016"),
        "exercicio017": st.session_state.get("exercicio017"),
        "exercicio018": st.session_state.get("exercicio018"),
        "exercicio019": st.session_state.get("exercicio019"),
        "exercicio020": st.session_state.get("exercicio020"),
        "exercicio021": st.session_state.get("exercicio021"),
        "exercicio022": st.session_state.get("exercicio022"),
        "exercicio023": st.session_state.get("exercicio023"),
        "exercicio024": st.session_state.get("exercicio024"),
        "exercicio025": st.session_state.get("exercicio025"),
        "exercicio026": st.session_state.get("exercicio026"),
        "exercicio027": st.session_state.get("exercicio027"),
        "exercicio028": st.session_state.get("exercicio028"),
        "exercicio029": st.session_state.get("exercicio029"),
        "exercicio030": st.session_state.get("exercicio030"),
        "exercicio031": st.session_state.get("exercicio031"),
        "exercicio032": st.session_state.get("exercicio032"),

        "exercicio001": st.session_state.get("exercicio001"),
        "exercicio002": st.session_state.get("exercicio002"),
        "exercicio003": st.session_state.get("exercicio003"),
        "exercicio004": st.session_state.get("exercicio004"),
        "exercicio005": st.session_state.get("exercicio005"),
        "exercicio006": st.session_state.get("exercicio006"),
        "exercicio007": st.session_state.get("exercicio007"),
        "exercicio008": st.session_state.get("exercicio008"),
        "exercicio009": st.session_state.get("exercicio009"),
        "exercicio0010": st.session_state.get("exercicio0010"),
        "exercicio0011": st.session_state.get("exercicio0011"),
        "exercicio0012": st.session_state.get("exercicio0012"),
        "exercicio0013": st.session_state.get("exercicio0013"),
        "exercicio0014": st.session_state.get("exercicio0014"),
        "exercicio0015": st.session_state.get("exercicio0015"),
        "exercicio0016": st.session_state.get("exercicio0016"),
        "exercicio0017": st.session_state.get("exercicio0017"),
        "exercicio0018": st.session_state.get("exercicio0018"),
        "exercicio0019": st.session_state.get("exercicio0019"),
        "exercicio0020": st.session_state.get("exercicio0020"),
        "exercicio0021": st.session_state.get("exercicio0021"),
        "exercicio0022": st.session_state.get("exercicio0022"),
        "exercicio0023": st.session_state.get("exercicio0023"),
        "exercicio0024": st.session_state.get("exercicio0024"),
        "exercicio0025": st.session_state.get("exercicio0025"),
        "exercicio0026": st.session_state.get("exercicio0026"),
        "exercicio0027": st.session_state.get("exercicio0027"),
        "exercicio0028": st.session_state.get("exercicio0028"),
        "exercicio0029": st.session_state.get("exercicio0029"),
        "exercicio0030": st.session_state.get("exercicio0030"),
        "exercicio0031": st.session_state.get("exercicio0031"),
        "exercicio0032": st.session_state.get("exercicio0032"),

    }
    st.session_state["dados_treino"] = dados_treino3

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

    if st.session_state.get("Quadriceps", True) or \
        st.session_state.get("PosteriorCoxa", True) or \
        st.session_state.get("Peito", True) or \
        st.session_state.get("Costas", True) or \
        st.session_state.get("Ombros", True) or \
        st.session_state.get("Triceps", True) or \
        st.session_state.get("Biceps", True) or \
        st.session_state.get("Gluteos", True):
        # Botão para gerar PDF
        if st.button("Gerar PDF"):
            from pdf import gerar_pdf3
            gerar_pdf3(st.session_state["dados_treino"])


        pdf_buffer3 = gerar_pdf3(dados_treino3).getvalue()

        #  Botão para download do PDF

        st.download_button(
            label="Baixar PDF",
            data=pdf_buffer3,
            file_name="FichaTreino.pdf",
            mime="pdf",
            key="download_pdf_button"
                )