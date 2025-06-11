import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Função para gerar o PDF

def gerar_pdf1(dados_treino1):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    pdf.drawImage("fundo01.jpg", 0, 0, width=width, height=height)

    grupos_todos = [
        ("Quadríceps", "Quadriceps", 0),
        ("Posterior de Coxa + Glúteos", "PosteriorCoxa", 4),
        ("Peito", "Peito", 8),
        ("Costas", "Costas", 12),
        ("Ombro", "Ombros", 16),
        ("Tríceps", "Triceps", 20),
        ("Bíceps", "Biceps", 24)
    ]

    posicoes_por_qtd = {
        1: [(60, 500)],
        2: [(60, 600), (60, 400)],
        3: [(60, 650), (60, 450), (60, 250)],
        4: [(60, 650), (330, 650), (60, 400), (330, 400)],
        5: [(60, 650), (330, 650), (60, 500), (330, 500), (225, 350)],
        6: [(60, 650), (350, 650), (60, 500), (350, 500), (60, 350), (350, 350)],
        7: [(60, 650), (350, 650), (60, 500), (350, 500), (60, 350), (350, 350), (225, 200)],
    }

    grupos_selecionados = [
        (nome, inicio)
        for nome, checkbox, inicio in grupos_todos
        if st.session_state.get(checkbox, False)
    ]

    n_grupos = len(grupos_selecionados)
    posicoes = posicoes_por_qtd.get(n_grupos, [])

    # Defina o tamanho da fonte conforme a quantidade de grupos
    if n_grupos == 1:
        font_titulo = 30
        font_exercicio = 24
    elif n_grupos == 2:
        font_titulo = 30
        font_exercicio = 24
    elif n_grupos == 3:
        font_titulo = 30
        font_exercicio = 24
    elif n_grupos == 4:
        font_titulo = 20
        font_exercicio = 14
    elif n_grupos == 5:
        font_titulo = 18
        font_exercicio = 14
    elif n_grupos == 6:
        font_titulo = 18
        font_exercicio = 14
    else:
        font_titulo = 14
        font_exercicio = 12

    for idx, (grupo, inicio) in enumerate(grupos_selecionados):
        if idx >= len(posicoes):
            break
        x, y = posicoes[idx]
        pdf.setFont("Times-Bold", font_titulo)
        pdf.drawString(x, y, grupo)
        y_ = y - 25 # Posição inicial para os exercícios
        pdf.setFont("Times-Roman", font_exercicio)
        for i in range(inicio, inicio+4):
            exercicio = dados_treino1.get(f"exercicio{i+1}", "")
            series = dados_treino1.get(f"series{i+1}", "")
            pdf.drawString(x + 10, y_, f"{exercicio} - {series}")
            y_ -= 30 # Espaço entre os exercícios

    pdf.save()
    buffer.seek(0)
    return buffer

## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
def gerar_pdf2(dados_treino2):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    pdf.drawImage("fundo02.jpg", 0, 0, width=width, height=height)

    grupos_todos = [
        ("Quadríceps", "Quadriceps", 0),
        ("Posterior de Coxa + Glúteos", "PosteriorCoxa", 4),
        ("Peito", "Peito", 8),
        ("Costas", "Costas", 12),
        ("Ombro", "Ombros", 16),
        ("Tríceps", "Triceps", 20),
        ("Bíceps", "Biceps", 24)
    ]

    posicoes_por_qtd = {
        1: [(60, 500)],
        2: [(60, 600), (60, 350)],
        3: [(120, 670), (120, 450), (120, 230)],
        4: [(20, 650), (330, 650), (20, 500), (330, 500)],
        5: [(20, 670), (330, 670), (20, 500), (330, 500), (225, 330)],
        6: [(20, 670), (350, 670), (20, 520), (350, 520), (20, 370), (350, 370)],
        7: [(20, 650), (350, 650), (20, 500), (350, 500), (20, 350), (350, 350), (225, 200)],
    }

    grupos_selecionados = [
        (nome, inicio)
        for nome, checkbox, inicio in grupos_todos
        if st.session_state.get(checkbox, False)
    ]

    n_grupos = len(grupos_selecionados)
    posicoes = posicoes_por_qtd.get(n_grupos, [])

    # Defina o tamanho da fonte conforme a quantidade de grupos
    if n_grupos == 1:
        font_titulo = 30
        font_exercicio = 20
    elif n_grupos == 2:
        font_titulo = 30
        font_exercicio = 20
    elif n_grupos == 3:
        font_titulo = 24
        font_exercicio = 18
    elif n_grupos == 4:
        font_titulo = 20
        font_exercicio = 14
    elif n_grupos == 5:
        font_titulo = 18
        font_exercicio = 14
    elif n_grupos == 6:
        font_titulo = 18
        font_exercicio = 14
    else:
        font_titulo = 18
        font_exercicio = 14

    for idx, (grupo, inicio) in enumerate(grupos_selecionados):
        if idx >= len(posicoes):
            break
        x, y = posicoes[idx]
        pdf.setFont("Times-Bold", font_titulo)
        pdf.drawString(x, y, grupo)
        y_ = y - 15  # Posição inicial para os exercícios
        pdf.setFont("Times-Roman", font_exercicio)
        for i in range(inicio, inicio+4):
            exercicio = dados_treino2.get(f"exercicio{i+1}", "")
            series = dados_treino2.get(f"series{i+1}", "")
            pdf.drawString(x + 10, y_, f"{exercicio} - {series}")
            y_ -= 10  # Espaço entre os exercícios

            # Inclui o extra se existir
            exercicio_extra = dados_treino2.get(f"exercicio0{i+1}", "")
            if exercicio_extra:
                pdf.drawString(x + 10, y_, f"{exercicio_extra}")
                y_ -= 20  # Espaço extra para o extra

    pdf.save()
    buffer.seek(0)
    return buffer


## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##
## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##  ## ===========  ## ## ===========  ##

def gerar_pdf3(dados_treino3):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    pdf.drawImage("fundo02.jpg", 0, 0, width=width, height=height)

    grupos_todos = [
        ("Quadríceps", "Quadriceps", 0),
        ("Posterior de Coxa + Glúteos", "PosteriorCoxa", 4),
        ("Peito", "Peito", 8),
        ("Costas", "Costas", 12),
        ("Ombro", "Ombros", 16),
        ("Tríceps", "Triceps", 20),
        ("Bíceps", "Biceps", 24)
    ]

    posicoes_por_qtd = {
        1: [(60, 500)],
        2: [(60, 600), (60, 350)],
        3: [(120, 670), (120, 450), (120, 230)],
        4: [(20, 650), (330, 650), (20, 400), (330, 400)],
        5: [(20, 670), (330, 670), (20, 450), (330, 450), (225, 225)],
        6: [(20, 670), (350, 670), (20, 450), (350, 450), (20, 0 ), (350, 225)],
        7: [(20, 670), (350, 670), (20, 450), (350, 450), (20, 0), (350, 225), (225, 225)],
    }

    grupos_selecionados = [
        (nome, inicio)
        for nome, checkbox, inicio in grupos_todos
        if st.session_state.get(checkbox, False)
    ]

    n_grupos = len(grupos_selecionados)
    posicoes = posicoes_por_qtd.get(n_grupos, [])

    # Defina o tamanho da fonte conforme a quantidade de grupos
    if n_grupos == 1:
        font_titulo = 30
        font_exercicio = 20
    elif n_grupos == 2:
        font_titulo = 30
        font_exercicio = 20
    elif n_grupos == 3:
        font_titulo = 24
        font_exercicio = 18
    elif n_grupos == 4:
        font_titulo = 20
        font_exercicio = 14
    elif n_grupos == 5:
        font_titulo = 20
        font_exercicio = 14
    elif n_grupos == 6:
        font_titulo = 20
        font_exercicio = 14
    else:
        font_titulo = 20
        font_exercicio = 14

    # Defina posições para cada página (exemplo para até 2 páginas)
    posicoes_por_pagina = [
    [  # Página 1
        (20, 650),   # 1º grupo da página 1
        (330, 650),  # 2º grupo da página 1
        (20, 400),   # 3º grupo da página 1
        (330, 400),  # 4º grupo da página 1
        (225, 10),  # 5º grupo da página 1
        (350, 225),  # 6º grupo da página 1
        (20, 225)    # 7º grupo da página 1
    ],
    [  # Página 2
        (60, 700),   # 1º grupo da página 2
        (330, 700),  # 2º grupo da página 2
        (60, 500),   # 3º grupo da página 2
        (330, 500),  # 4º grupo da página 2
        (120, 650),  # 5º grupo da página 2
        (120, 470),  # 6º grupo da página 2
        (120, 250)   # 7º grupo da página 2
    ],  # Adicione mais páginas se precisar
    ]

    pagina_atual = 0

    for idx, (grupo, inicio) in enumerate(grupos_selecionados):
        # Use a posição da página atual
        posicoes = posicoes_por_pagina[pagina_atual]
        if idx >= len(posicoes):
            break
        x, y = posicoes[idx]
        pdf.setFont("Times-Bold", font_titulo)
        pdf.drawString(x, y, grupo)
        y_ = y - 25
        pdf.setFont("Times-Roman", font_exercicio)
        for i in range(inicio, inicio+4):
            exercicio = dados_treino3.get(f"exercicio{i+1}", "")
            series = dados_treino3.get(f"series{i+1}", "")
            pdf.drawString(x + 10, y_, f"{exercicio} - {series}")
            y_ -= 15

            exercicio_extra = dados_treino3.get(f"exercicio0{i+1}", "")
            if exercicio_extra:
                pdf.drawString(x + 10, y_, f"{exercicio_extra}")
                y_ -= 15

            exercicio_extra2 = dados_treino3.get(f"exercicio00{i+1}", "")
            if exercicio_extra2:
                pdf.drawString(x + 10, y_, f"{exercicio_extra2}")
                y_ -= 15

            y_ -= 3

            # Se o espaço acabar, muda para a próxima página e usa novas posições
            if y_ < 30:
                pdf.showPage()
                pdf.drawImage("fundo02.jpg", 0, 0, width=width, height=height)
                pagina_atual += 1
                # if pagina_atual >= len(posicoes_por_pagina):
                #     pagina_atual = len(posicoes_por_pagina) - 1  # Evita erro se faltar página
                posicoes = posicoes_por_pagina[pagina_atual]
                x, y = posicoes[idx]
                pdf.setFont("Times-Bold", font_titulo)
                pdf.drawString(x, y, grupo + " (cont.)")
                y_ = y - 10
                pdf.setFont("Times-Roman", font_exercicio)

    pdf.save()
    buffer.seek(0)
    return buffer
