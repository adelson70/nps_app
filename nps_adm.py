# Importando biblioteca
import tkinter as tk
from tkinter.font import Font
import sqlite3 as sql


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

janela.mainloop()