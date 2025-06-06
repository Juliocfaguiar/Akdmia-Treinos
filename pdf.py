import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Função para gerar o PDF

def gerar_pdf1(dados_treino1):
    """
    Gera um PDF com os Treinos selecionados.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    # Defina a cor de fundo (por exemplo, azul claro)
    # pdf.setFillColorRGB(0.3, 0.3, 0.3)  # RGB entre 0 e 1
    # pdf.rect(0, 0, width, height, fill=1, stroke=0)  # Desenha o fundo
    pdf.setFont("Times-Roman", 12)
    y = 700  # Posição inicial vertical


    pdf.drawImage("Logo akdmia do joel.png", x=20, y=650, width=150, height=100)
    pdf.drawImage("Logo akdmia do joel.png", x=430, y=650, width=150, height=100)
    pdf.drawImage("fichadetreino.png", x=150, y=650, width=300, height=100)

     # Defina as posições iniciais (x, y) para cada grupo
    grupos = [
        ("Quadríceps", 0, 50, 550),
        ("Posterior de Coxa + Glúteos", 4, 350, 550),
        ("Peito", 8, 50, 430),
        ("Costas", 12, 350, 430),
        ("Ombro", 16, 50, 310),
        ("Tríceps", 20, 350, 310),
        ("Bíceps", 24, 225, 190)
    ]

    for grupo, inicio, x, y in grupos:
        pdf.setFont("Times-Bold", 18)
        pdf.drawString(x, y, grupo)
        y -= 25  # Espaçamento entre o título do grupo e os exercícios
        pdf.setFont("Times-Roman", 12)
        for i in range(inicio, inicio+4):
            exercicio = dados_treino1.get(f"exercicio{i+1}", "")
            series = dados_treino1.get(f"series{i+1}", "")
            pdf.drawString(x + 10, y, f"{exercicio} - {series}")
            y -= 20  # Ajuste o espaçamento entre as linhas conforme necessário

    pdf.save()
    buffer.seek(0)
    return buffer

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

def gerar_pdf2(dados_treino2):
    """
    Gera um PDF com os Treinos selecionados.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    # Defina a cor de fundo (por exemplo, azul claro)
    # pdf.setFillColorRGB(0.3, 0.3, 0.3)  # RGB entre 0 e 1
    # pdf.rect(0, 0, width, height, fill=1, stroke=0)  # Desenha o fundo
    pdf.setFont("Times-Roman", 12)
    y = 700  # Posição inicial vertical


    pdf.drawImage("Logo akdmia do joel.png", x=20, y=650, width=150, height=100)
    pdf.drawImage("Logo akdmia do joel.png", x=430, y=650, width=150, height=100)
    pdf.drawImage("fichadetreino.png", x=150, y=650, width=300, height=100)

   
     # Defina as posições iniciais (x, y) para cada grupo
    grupos = [
        ("Quadríceps", 0, 50, 600),
        ("Posterior de Coxa + Glúteos", 4, 350, 600),
        ("Peito", 8, 50, 450),
        ("Costas", 12, 350, 450),
        ("Ombro", 16, 50, 300),
        ("Tríceps", 20, 350, 300),
        ("Bíceps", 24, 225, 150),
    ]

    for grupo, inicio, x, y in grupos:
        pdf.setFont("Times-Bold", 18)
        pdf.drawString(x, y, grupo)
        y -= 25
        pdf.setFont("Times-Roman", 12)
        for j in range(4):
            idx = inicio + j + 1
            exercicio = dados_treino2.get(f"exercicio{idx}", "")
            series = dados_treino2.get(f"series{idx}", "")
            pdf.drawString(x + 10, y, f"{exercicio} - {series}")
            y -= 10
            # Mostra o extra se existir
            exercicio_extra = dados_treino2.get(f"exercicio0{idx}", "")
            if exercicio_extra:
                pdf.drawString(x + 10, y, f"{exercicio_extra}")
            y -= 20  # Ajuste o espaçamento entre as linhas conforme necessário


    pdf.save()
    buffer.seek(0)
    return buffer

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

def gerar_pdf3(dados_treino3):
    """
    Gera um PDF com os Treinos selecionados.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    # Defina a cor de fundo (por exemplo, azul claro)
    # pdf.setFillColorRGB(0.3, 0.3, 0.3)  # RGB entre 0 e 1
    # pdf.rect(0, 0, width, height, fill=1, stroke=0)  # Desenha o fundo
    pdf.setFont("Times-Roman", 12)
    y = 700  # Posição inicial vertical


    pdf.drawImage("Logo akdmia do joel.png", x=20, y=690, width=150, height=100)
    pdf.drawImage("Logo akdmia do joel.png", x=430, y=690, width=150, height=100)
    pdf.drawImage("fichadetreino.png", x=150, y=690, width=300, height=100)

    grupos = [
        ("Quadríceps", 0, 50, 680),
        ("Posterior de Coxa + Glúteos", 4, 350, 680),
        ("Peito", 8, 50, 510),
        ("Costas", 12, 350, 510),
        ("Ombro", 16, 50, 340),
        ("Tríceps", 20, 350, 340),
        ("Bíceps", 24, 225, 170)
    ]

    for grupo, inicio, x, y in grupos:
        pdf.setFont("Times-Bold", 14)
        pdf.drawString(x, y, grupo)
        y -= 10
        pdf.setFont("Times-Roman", 10)
        for j in range(4):  # ou 5, se quiser mais exercícios
            idx = inicio + j + 1
            exercicio = dados_treino3.get(f"exercicio{idx}", "")
            series = dados_treino3.get(f"series{idx}", "")
            pdf.drawString(x + 10, y, f"{exercicio} - {series}")
            y -= 10

            # Mostra o extra se existir
            exercicio_extra = dados_treino3.get(f"exercicio0{idx}", "")
            if exercicio_extra:
                pdf.drawString(x + 10, y, f"{exercicio_extra}")
                y -= 10  # Espaço entre linhas extras

            # Mostra o segundo extra se existir
            exercicio_extra2 = dados_treino3.get(f"exercicio00{idx}", "")
            if exercicio_extra2:
                pdf.drawString(x + 10, y, f"{exercicio_extra2}")
                y -= 10  # Espaço entre linhas extras
            y -= 10  # Ajuste o espaçamento entre as linhas conforme necessário


    pdf.save()
    buffer.seek(0)
    return buffer