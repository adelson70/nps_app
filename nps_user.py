import tkinter as tk

def avaliacao(nivel_satisfacao):
    print("Nível de satisfação selecionado:", nivel_satisfacao)

# GUI
janela = tk.Tk()
janela.title('Avaliação de Satisfação')
janela.geometry('400x200')

# Labels
titulo = tk.Label(janela, text='Avalie sua Experiência')
titulo.pack(pady=5)

# Buttons
botoes_satisfacao = []
for i in range(1, 11):
    botao = tk.Button(janela, text=str(i), command=lambda nivel=i: avaliacao(nivel))
    botoes_satisfacao.append(botao)
    botao.pack(side=tk.LEFT, padx=1, pady=5)  # Adicionando os botões lado a lado

janela.mainloop()
