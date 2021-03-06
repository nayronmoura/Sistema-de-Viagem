import menus
from Motoristas import motoristaBanco as banco
import re

CPFexpr = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')  # expressão regular- É um padrão para strings


def main():
    print(" \n ")
    menus.menu_motorista()
    chose = int(input("Selecione uma opção: "))
    match chose:
        case 1:
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


def adicionar():
    print("-" * 30)
    while True:
        print('Digite o CPF com letras e pontos ex: 999.999.999-99')
        cpf = input("Qual o CPF?  ")
        if CPFexpr.match(cpf):  # checa se a string está seguindo o padrão do CPF
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
        if carteira.upper() in "AB":
            break
        else:
            print("A carteira selecionada não é válida tente novamente.")

    banco.adicionar({'cpf': cpf, 'nome': nome, 'carteira': carteira.upper()})

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
    print("-" * 30)
    while True:
        cpf = input("Qual o cpf? ")
        if CPFexpr.match(cpf):  # checa se a string está seguindo o padrão do CPF
            if banco.checkCPF(cpf):
                resultado = banco.pegarCPF(cpf)
                if len(resultado) > 0:
                    print(f'''
                        Nome: {resultado.get('nome')}
                        CPF: {resultado.get('cpf')}
                        Carteira: {resultado.get('carteira')}
                    ''')
                    print("-" * 30)
                    break
                else:
                    print('não há dados no banco.')
                    print("-" * 30)
            else:
                print("CPF não encontrado, Digite novamente.")
                print("-" * 30)
        else:
            print("CPF digitado incorretamente. siga o padrão 999.999.999-99")
            print("-" * 30)
    main()


def editar():
    print("-" * 30)
    while True:
        cpf = input("Qual o CPF do Motorista? ")
        if CPFexpr.match(cpf):
            if banco.checkCPF(cpf):
                nome = str(input("Qual o novo nome? "))
                print(banco.altera(cpf, nome))
                print("-" * 30)
                break
            else:
                print("O cpf não está cadastrado.")
                print("-" * 30)
        else:
            print("CPF digitado incorretamente ou não cadastrado. siga o padrão 999.999.999-99")
            print("-" * 30)
    main()


def remover():
    print("-" * 30)
    cpf = input("Qual o CPF do Motorista? ")
    if CPFexpr.match(cpf):
        if banco.checkCPF(cpf):
            motorista = banco.pegarCPF(cpf)
            while True:
                escolha = int(input(f"Deseja realmente excluir {motorista.get('name')}?\n [1]- Sim \n[2]- Não \n:   "))
                if escolha == 1:
                    banco.remover(cpf)
                    print('Removido com sucesso.')
                    print("-" * 30)
                    break
                elif escolha == 2:
                    print('Operação cancelada.')
                    print("-" * 30)
                    break
                else:
                    print('Selecione uma opção válida')
                    print("-" * 30)
        else:
            print("O cpf não está cadastrado.")
            print("-" * 30)
    else:
        print("CPF digitado incorretamente. siga o padrão 999.999.999-99")
        print("-" * 30)
    main()


def listarFiltrado():
    print("-" * 30)
    carteira = input('Qual carteira deseja filtrar? [A] [B] [AB]  ')
    motoristas = banco.pegarTodos()
    if len(motoristas) > 0:
        for motorista in motoristas:
            if motorista.get('carteira') == carteira:
                print(f'''
                {'' * 20}Nome: {motorista.get('nome')}
                {'' * 20}CPF: {motorista.get('cpf')}
                {'' * 20}Carteira: {motorista.get('carteira')}''')
        print("-" * 30)
    else:
        print('Não há motoristas cadastrados.')
        print("-" * 30)
    main()


def listarTodos():
    print("-" * 30)
    motoristas = banco.pegarTodos()
    if len(motoristas) > 0:
        for motorista in motoristas:
            print(f'''
                   {'' * 20}Nome: {motorista.get('nome')}
                   {'' * 20}CPF: {motorista.get('cpf')}
                   {'' * 20}Carteira: {motorista.get('carteira')}
                   ''')
        print("-" * 30)
    else:
        print('Não há motoristas cadastrados.')
        print("-" * 30)
    main()
