import tkinter as tk
from tkinter.font import Font

def avaliacao(nivel_satisfacao):
    return saida_info(nivel_satisfacao)

def saida_info(satisfacao):

    return ...

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
