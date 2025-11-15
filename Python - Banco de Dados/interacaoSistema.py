from crud import Animacao, InteracaoBanco, ListarTabelas
import _sqlite3

def menu():
    #bloco 01
    igual = "="*20
    sistema = True

    #bloco 02
    while sistema != False:
        
        #bloco 03
        Animacao()
        
        #bloco 04
        print(igual,"seja bem vindo a aula de pythom com banco de dados",igual)
        
        nome = input("infome seu nome: ")
        sobrenome = input("informe seu sobre nome: ")
        idade = int(input("informe sua idade: "))

        #bloco 05
        conexao = _sqlite3.connect("abobrinha.sqlite")
        cursor = conexao.cursor()

        ListarTabelas(cursor, conexao)

        InteracaoBanco(nome, sobrenome, cursor, conexao)

        continuaSistema = int(input(f"deseja continuar no sistema\ndigite 1 para sim e 2 para nao: "))
        
        if continuaSistema == 2:
            sistema = False

        elif continuaSistema == 1:
            sistema = True

        else:
            print(f"o numero {continuaSistema} que voce digitou nao faz parte das opcoes fornecidas: ")
            sistema = False



    #bloco07
    Animacao()
    print('voce saiu do sistema')
    conexao.close()

