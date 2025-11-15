from time import sleep
import sqlite3


def Animacao():
    for animacao in range(20):
            sleep(0.1)
            print("*")

def ListarTabelas(cursor, conexao):
     conexao = sqlite3.connect("abobrinha.sqlite")
     cursor = conexao.cursor()

     listarTabelas = "SELECT name FROM sqlite_master WHERE type='table';"

     cursor.execute(listarTabelas)

     tabelas = cursor.fetchall()

     if tabelas:
      for tabela in tabelas:
        print("Tabela", tabela[0])

     else: 
      print("nenhuma Tabela encontrada no banco atual")
     
                 
                

def InteracaoBanco(nome, sobrenome, cursor, conexao):
 #bloco 06
        repeticao = True

        nomeTabela = input(f"informe o nome da tabela que deseja criar: ")

        colunas = []

        for i in range(1, 3):
            print(f"\n--- Coluna{i} ---")
            nomecoluna = input(f"{nome}, informe o nome da coluna {i}: ")

            print("\n INTEGER\n TEXT\n REAL\n NUMERIC\n")
            tipocoluna = input(f"{nome}, informe o tipo da coluna {i}: ")

            print("\n NOT NULL\n NULL")
            colunaVazio = input(f"{nome}, informe se a coluna poder ser nula ou não")

            colunas.append(f"{nomecoluna} {tipocoluna} {colunaVazio}")

            comandoCriaTabela = f"""
            CREATE TABLE IF NOT EXISTS {nomeTabela} (
                {',' .join(colunas)}
            )
            """


                

            cursor.execute(comandoCriaTabela)
            conexao.commit()

                



            desejaDeletar = True

            while desejaDeletar != False:

                    deleta = int(input(f"{nome}{sobrenome}, deseja deletar a tabela?\ndigite 1 para sim e 2 para nao: "))

                    if deleta == 1:
                        desejaDeletar = False
                        comandoDeletaTabela = f'''
                            DROP TABLE {nomeTabela}
                            '''
                        print(f"a tabela {nomeTabela} foi excluida")

                        cursor.execute(comandoDeletaTabela)
                        conexao.commit()


                    elif deleta == 2:
                        desejaDeletar = False
                        print(f"a tabela {nomeTabela} nao sera excluida: ")

                    else:
                        print(f"o numero {deleta} que voce digitou nao faz parte das informacoes fornecidas ")
                        desejaDeletar = True

            else:
                repeticao = True
                print(f"o numero {nomeTabela} que voce digitou nao faz parte das informacoes fornecidas ")
