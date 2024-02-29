import tkinter as tk
from tkinter.font import Font
from datetime import datetime
import sqlite3 as sql

# vão ter 2 dbs
# um como historico
# e outro como uma linha somente, sem data e hora

# Função principal onde chamara as outras funções e tambem fara o calculo do NPS
def avaliacao(nivel_satisfacao):
    data_completa = get_data()
    horario_completo = get_horario()
    cursorHistdb, conexaoHistdb = db_hist()
    cursorNPS, conexaoNPS = db_nps()

    # Incrementando a tabela de historico de avaliacoes
    cursorHistdb.execute("""
                         INSERT INTO histAvaliacoes(data, horario, avaliacao)
                         VALUES (?,?,?)""",(data_completa, horario_completo, nivel_satisfacao))
    conexaoHistdb.commit()

    # Consultando a quantidade de detratores
    cursorHistdb.execute("SELECT COUNT(*) FROM histAvaliacoes WHERE avaliacao BETWEEN 0 AND 6")
    detratores = cursorHistdb.fetchone()[0]
    
    # Consultando a quantidade de neutros
    cursorHistdb.execute("SELECT COUNT(*) FROM histAvaliacoes WHERE avaliacao BETWEEN 7 AND 8")
    neutros = cursorHistdb.fetchone()[0]
    
    # Consultando a quantidade de promotores
    cursorHistdb.execute("SELECT COUNT(*) FROM histAvaliacoes WHERE avaliacao BETWEEN 9 AND 10")
    promotores = cursorHistdb.fetchone()[0]

    # Calculo para descobrir o NPS
    total_avaliacoes = detratores+neutros+promotores
    nps = f'{int(((promotores - detratores) / total_avaliacoes) * 100)}' if total_avaliacoes > 0 else 0

    print(detratores, neutros, promotores, nps)
    # Atualizando a tabela de NPS    
    cursorNPS.execute("""
                  UPDATE nps 
                  SET promotores=?, neutros=?, detratores=?, nps=?
                  """, (promotores, neutros, detratores, nps))

    conexaoNPS.commit()

    cursorNPS.execute('select * from nps')
    for l in cursorNPS.fetchall():
        print(l)

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

# Banco de dados com historico de avaliacoes
def db_hist():
    conexao = sql.connect('histAvaliacao.db')
    cursor = conexao.cursor()
    
    # Verifica se o banco de dados já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='histAvaliacoes'")
    tabela_existe = cursor.fetchone()

    if tabela_existe:
        return (cursor, conexao)
    
    else:
        # Cria a tabela de dados
        cursor.execute("""
CREATE TABLE histAvaliacoes
(data DATE,
horario TIME,
avaliacao INTEGER)""")

        return (cursor, conexao)
    
# Banco de dados NPS
def db_nps():
    conexao = sql.connect('nps.db')
    cursor = conexao.cursor()
    
    # Verifica se o banco de dados já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='nps'")
    tabela_existe = cursor.fetchone()

    if tabela_existe:
        return (cursor, conexao)
    
    else:
        # Cria a tabela de dados
        cursor.execute("""
CREATE TABLE nps
(promotores INTEGER DEFAULT 0,
neutros INTEGER DEFAULT 0,
detratores INTEGER DEFAULT 0,
nps INTEGER DEFAULT 0)""")
        
        # Forçando a criação default 
        cursor.execute("SELECT COUNT(*) FROM nps")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""INSERT INTO nps(promotores, neutros, detratores, nps) 
                           VALUES(?,?,?,?)""",(0, 0, 0, 0))
        conexao.commit()
        
        return (cursor, conexao)
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
