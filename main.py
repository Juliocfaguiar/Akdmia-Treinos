import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf import gerar_pdf1, gerar_pdf2, gerar_pdf3


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

posteriorCoxa = ["Stiff com barra", "Stiff com halteres", "Stiff unilateral com halteres", "Afundo com halteres", "Terra com pernas rígidas", "Bom dia com barra", "Flexão nórtica", "Mesa flexora", "Cadeira flexora", "Flexora em pé", "Elevação pélvica", "Leg press 45º com os pés altos", "Hack machine com os pés altos", "Extensão de quadril com tornozeleira", "Extensão de quadril no banco",  "Extensão de quadril no cross", "Elevação pélvica unilateral", "Abdução de quadril em pé", "Abdução de quadril deitada", "cadeira abdutora", "cadeira adutora", "Chute para trás no cross","Chute lateral no cross", "Chute para trás com caneleira", "Chute lateral com caneleira", "Afundo no step", "Passada lateral", "Passada cruzada", "Passada cruzada com halteres", "Agachamento frog pump", "Fire hydrant", "Donkey kicks com caneleira"]

peito=["Supino reto com barra", "Supino inclinado com barra", "Supino declinado com barra", "Supino reto com pegada fechada", "Supino reto com halteres", "Supino inclinado com halteres", "Supino declinado com halteres", "Crucifixo reto com halteres", "Crucifixo inclinado com halteres", "Crucifixo declinado com halteres", "Supino com giro", "Pec deck", "peck deck unilateral", "Máquina com pegada neutra", "Cross-over alto", "Cross-over baixo", "Cross-over na linha do peito", "Crucifixo com polia baixa", "Crucifixo com polia alta"]

costas = ["Pulley frente", "Pulley triângulo", "Pulley unilateral", "Remada sentado com triângulo", "Remada sentado com barra", "Remada sentado unilateral", "Remada baixa", "Remada alta", "Remada na máquina Hammer", "Remada na máquina Hammer uni", "Remada curvada com barra", "Remada curvada com halteres", "Remada serrote", "Pulldown com barra", "Pulldown com corda", "Pulldown com triângulo"]

ombros = ["Desenvolvimento frontal com barra", "Elevação frontal com barra", "Desenvolvimento frontal com halteres", "Arnold press", "Elevação frontal com halteres", "Elevação frontal com halteres alternado", "Elevação lateral com halteres", "Elevação lateral com halteres alternado", "Crucifixo invertido com halteres", "Crucifixo invertido com halteres alternado", "Elevação martelo alternada", "Elevação martelo total", "Elevação lateral na polia", "Elevação frontal na polia", "Face pull com corda", "Remada alta na polia baixa", "Crucifixo invertido na máquina peck deck"]

triceps = ["francês unilateral com halteres", "Tríceps kickback com halteres", "Pullover com halteres", "Pulley com barra", "Pulley com corda", "Pulley unilateral com corda", "Pulley inverso com barra", "Pulley inverso com puxador", "Tríceps testa com barra", "Overhead com barra na polia", "Overhead com corda na polia", "Mergulho no banco"]

biceps = ["Rosca direta com barra reta", "Rosca direta com barra W", "Rosca 21", "Rosca no banco Scott", "Rosca no banco Scott alternado", "Rosca alternada com halteres", "Rosca simultânea com halteres", "Rosca martelo com halteres", "Rosca concentrada com halteres", "Rosca cruzada com halteres", "Rosca inclinada total", "Rosca inclinada alternada", "Rosca com corda na polia", "Rosca Zottman", "Rosca inversa com barra", "Rosca inversa com halteres", "Rosca de punho com barra", "Rosca de punho com halteres", "Rosca de punho invertida com halteres"]

series = ["4*8","4*10","4*12","4*15","4*20","4*8~12","5*8","5*10","5*12","5*15","5*20","5*8~12","6*8","6*10","6*12","6*15","6*20","6*8~12","7*8","7*10","7*12","7*15","7*20","7*8~12","8*8","8*10","8*12","8*15","8*20","8*8~12","9*8","9*10","9*12","9*15","9*20","9*8~12","10*8","10*10","10*12","10*15","10*20","10*8~12","1*200"]

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

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
    st.subheader("Posterior de Coxa + Clúteos",divider="gray")
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
    }
    st.session_state["dados_treino"] = dados_treino1

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


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
        segundo = st.selectbox("4", options=costas, key="exercicio016")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series16")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
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
    }
    st.session_state["dados_treino"] = dados_treino2

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


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
        segundo = st.selectbox("4", options=costas, key="exercicio016")
        segundo = st.selectbox("4", options=costas, key="exercicio0016")
    with col2:
        segundo_series = st.selectbox("Séries/Repetições", options=series, key="series16")

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
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

    }
    st.session_state["dados_treino"] = dados_treino3

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##


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