import _sqlite3

conexao = _sqlite3.connect("abobrinha.sqlite")
cursor = conexao.cursor()


comando = "SELECT name FROM sqlite_master WHERE type='table';"

cursor.execute(comando)

tabelas = cursor.fetchall()

if tabelas:
    for tabela in tabelas:
        print('Tabela:', tabela[0])
else:
    print('Nenhuma tabela encontrada no banco atual')        


conexao.close()