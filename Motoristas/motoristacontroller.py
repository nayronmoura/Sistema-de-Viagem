import menus
import motoristaBanco as banco
import re
<<<<<<< HEAD
import main
=======

banco = motoristaBanco
CPFexpr = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')#expressão regular- É um padrão para strings

>>>>>>> 4657debb4722b06553627b275c89d839e4f8ed26

def main():
    menus.menu_motorista()
    chose = int(input("Selecione uma opção: "))
    match chose:
        case 1:
            global CPFexpr;
            CPFexpr = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}') # expressão regular - É um padrão para strings
            adicionar()
        case 2:
            resgatar()
        case 3:
            editar()
        case 4:
            remover()
        case 5:
            listarFiltrado()
        case 6:
            listarTodos()
        case 7:
            Main.init()

def adicionar():
    while True:
        print('Digite o CPF com letras e pontos ex: 999.999.999-99')
        cpf = input("Qual o CPF?  ")
        if CPFexpr.match(cpf): #checa se a string está seguindo o padrão do CPF
            if banco.checkCPF(cpf):
                print("O cpf já está cadastrado.")
            else:
                break
        else:
            print('O CPF foi digitado incorretamente.')

    nome = str(input("Insira o nome do Motorista: "))

    while True:
        print('''Qual a Carteira do Motorista? A, B ou AB
        ''')
        carteira = str(input("Digite a carteira: "))
        if carteira in "AB":
            break
        else:
            print("A carteira selecionada não é válida tente novamente.")

    banco.adicionar({'cpf': cpf, 'nome': nome, 'carteira': carteira})

    while True:
        escolha = str(input("Deseja adicionar mais um Motorista? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")
    main()

def resgatar():
    while True:
        cpf = input("Qual o cpf? ")
        if CPFexpr.match(cpf): #checa se a string está seguindo o padrão do CPF
            if banco.checkCPF(cpf):
                resultado = banco.pegarCPF(cpf)
                print(f'''
                    Nome: {resultado.get('nome')}
                    CPF: {resultado.get('cpf')}
                    Carteira: {resultado.get('carteira')}
                ''')
            else:
                print("CPF não encontrado, Digite novamente.")
        else:
            print("CPF digitado incorretamente. siga o padrão 999.999.999-99")
    main()

def editar():
    cpf = input("Qual o CPF do Motorista? ")
    if CPFexpr.match(cpf):
        if banco.checkCPF(cpf):
            nome = str(input("Qual o novo nome? "))
            print(banco.altera(cpf, nome))
        else:
            print("O cpf não está cadastrado.")
    else:
        print("CPF digitado incorretamente. siga o padrão 999.999.999-99")
    main()

def remover():
    cpf = input("Qual o CPF do Motorista? ")
    if CPFexpr.match(cpf):
        if banco.checkCPF(cpf):
            motorista = banco.pegarCPF(cpf)
            while True:
                escolha = int(input(f"Deseja realmente excluir {motorista.get('name')}?\n [1]- Sim \n[2]- Não \n:   "))
                if escolha == 1:
                    banco.remover(cpf)
                    print('Removido com sucesso.')
                    break
                elif escolha == 2:
                    print('Operação cancelada.')
                    break
                else:
                    print('Selecione uma opção válida')
        else:
            print("O cpf não está cadastrado.")
    else:
        print("CPF digitado incorretamente. siga o padrão 999.999.999-99")
    main()

def listarFiltrado():
    carteira = input('Qual carteira deseja filtrar? [A] [B] [AB]  ')
    motoristas = banco.pegarTodos()
    for motorista in motoristas:
        if motorista.get('carteira') == carteira:
            print(f'''
            {''*20}Nome: {motorista.get('nome')}
            {''*20}CPF: {motorista.get('cpf')}
            {''*20}Carteira: {motorista.get('carteira')}
            ''')
    main()

def listarTodos():
    motoristas = banco.pegarTodos()
    for motorista in motoristas:
            print(f'''
               {'' * 20}Nome: {motorista.get('nome')}
               {'' * 20}CPF: {motorista.get('cpf')}
               {'' * 20}Carteira: {motorista.get('carteira')}
               ''')
    main()

main()
