import tkinter as tk
from tkinter.font import Font
from datetime import datetime
import pandas as pd

# vão ter duas planilhas
# um como historico
# e outro como uma linha somente, sem data e hora

# Função principal onde chamara as outras funções e tambem fara o calculo do NPS
def avaliacao(nivel_satisfacao):
    data_completa = get_data()
    horario_completo = get_horario()
    df_hist = planilha_historica()
    df_nps = planilha_geral()

    # Incrementando avaliacoes na planilha historica
    df_hist['data']
    df_hist['horario']
    df_hist['avaliacao']
    

    print(df_nps.head())

# Função que retornar a data dd/mm/aaaa
def get_data():
    data_completa = datetime.now()
    dia = data_completa.day
    mes = data_completa.month
    ano = data_completa.year

    data_formatada = f'{dia:02}/{mes:02}/{ano}'
    return data_formatada

# Função que retorna o horario hh:mm
def get_horario():
    data_completa = datetime.now()
    hora = data_completa.hour
    minuto = data_completa.minute

    horario_formatado = f'{hora:02}:{minuto:02}'
    return horario_formatado

# Função que cria ou incrementa o banco de dados que é um historico das avalições
def planilha_historica():
    try:
        df = pd.read_csv('historico_avaliacoes.csv')

    except FileNotFoundError:
        df = pd.DataFrame(columns=['data','horario','avaliacao'])
        df['data'] = pd.to_datetime(df['data'])

    return df

# Função para criar a planilha com apenas 1 dado por coluna
def planilha_geral():
    try:
        df = pd.read_csv('avaliacoes.csv')

    except FileNotFoundError:
        df = pd.DataFrame(columns=['promotor','neutro','detrator','total','nps','status'])

    return df

# GUI
janela = tk.Tk()
janela.title('Avaliação de Satisfação')
janela.geometry('370x80')

# Fonts
fonte_titulo = Font(janela, family='Arial', weight='normal')
fonte_botoes = Font(janela, family='Arial', weight='normal')

# Bloqueando o redimensionamento
janela.resizable(width=False, height=False)

# Labels
titulo = tk.Label(janela, text='Avalie sua Experiência', font=fonte_titulo)
titulo.pack(pady=5)

# Buttons
botoes_satisfacao = []
for i in range(1, 11):
    botao = tk.Button(janela, text=str(i), font=fonte_botoes, command=lambda nivel=i: avaliacao(nivel))
    botoes_satisfacao.append(botao)
    botao.pack(side=tk.LEFT, padx=4, pady=5)  # Adicionando os botões lado a lado

janela.mainloop()
