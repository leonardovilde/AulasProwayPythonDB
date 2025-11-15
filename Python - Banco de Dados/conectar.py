import sqlite3

# 1 passo Interacao com usuario

#nome = input("Digite o Nome que deseja dar para seu Banco :>)

# cria um novo banco ou conecta a um banco existente

conexao = sqlite3.connect("Gislaine.sqlite")

#funcao Sqlite de manipulacao de script SQL
cursor = conexao.cursor()

comandoSQL = '''
CREATE TABLE IF NOT EXISTS produtos (
id INTEGER,
nome TEXT NOT NULL
)
'''

cursor.execute (comandoSQL)
conexao.commit()
conexao.close()