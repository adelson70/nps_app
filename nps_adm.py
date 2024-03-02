# Importando biblioteca
import tkinter as tk
from tkinter.font import Font
import sqlite3 as sql

# Função para atualizar a label
def atualizar_label(score):
    global janela
    global status
    global valor_nps

    # Atualiza a label do valor nps
    texto = f'NPS: {score}%'
    valor_nps.config(text=texto)

    # Atualiza o a label status conforme o criterio a baixo
    if score >= -100 and score <= -1:
        status_score = 'RUIM'

    elif score >= 0 and score <= 49:
        status_score = 'RAZOÁVEL'

    elif score >= 50 and score <= 74:
        status_score = 'MUITO BOM'

    else:
        status_score = 'EXCELENTE'

    status.config(text=status_score)

    janela.after(500, get_nps)

# Função para consultar o nps
def get_nps():
    global valor_nps
    try:
        conexao_nps = sql.connect('nps.db')
        cursor_nps = conexao_nps.cursor()

        cursor_nps.execute("SELECT nps FROM nps")
        nps_score = cursor_nps.fetchone()[0]
        
        atualizar_label(nps_score)

    except:
        print('Tabela não existe!')

# GUI
janela = tk.Tk()
janela.title('Avaliações')
janela.geometry('240x90')
janela.resizable(width=False, height=False)

# Fontes personalizadas
fonte_status = Font(janela, family='Arial', weight='normal', size=20)

# Labels
status = tk.Label(janela, text='BOM', font=fonte_status)
status.pack(pady=2)

valor_nps = tk.Label(janela, text='NPS: 70%', font=fonte_status)
valor_nps.pack(pady=3)

get_nps()

janela.mainloop()