from time import sleep


def Animacao():
    for animacao in range(20):
            sleep(0.1)
            print("*")


def InteracaoBanco(nome, sobrenome, cursor, conexao):
 #bloco 06
        repeticao = True

        while repeticao != False:
            
            novaTabela = int(input(f"{nome}{sobrenome},desja criar uma nova tabela\ndigite 1 para sim e 2 para nao"))

            if novaTabela == 2:
                repeticao = False

            elif novaTabela == 1:
                repeticao = True

                nomeTabela = input(f"{nome}{sobrenome},informe o nome da tabela que deseja criar: ")

                comandoCriaTabela = f'''
                CREATE TABLE IF NOT EXISTS {nomeTabela} (
                    ID INTEGER,
                    NOME TEXT NOT NULL
                )
                '''
                

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
                print(f"o numero {novaTabela} que voce digitou nao faz parte das informacoes fornecidas ")
