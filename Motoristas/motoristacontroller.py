import Menus
import motoristaBanco

banco = motoristaBanco


def main():
    Menus.menu_motorista()
    chose = int(input("Selecione uma opção: "))
    match chose:
        case 1:
            adicionar()
        case 2:
            resgatar()


def adicionar():
    while True:
        cpf = int(input("Qual o CPF? obs:apenas números "))
        if banco.checkCPF(cpf):
            print("O cpf já está cadastrado.")
        else:
            break

    nome = str(input("Insira o nome do Motorista: "))

    while True:
        print('''Qual a Carteira do Motorista? A, B ou AB
        ''')
        carteira = str(input("Digite a carteira: "))
        if carteira in "AB":
            break
        else:
            print("A carteira selecionada não é válida tente novamente.")

    motorista = {'cpf': cpf, 'nome': nome, 'carteira': carteira}
    banco.adicionar(motorista)

    while True:
        escolha = str(input("Deseja adicionar mais um Motorista? [S] [N]"))
        if escolha.upper() == 'S':
            adicionar()
        elif escolha.upper() == 'N':
            break
        else:
            print("Digite S para sim e N para não.")


def resgatar():
    cpf = int(input("Qual o cpf? "))
    resultado = banco.pegar(cpf)
    print(f'''
        Nome: {resultado.get('nome')}
        CPF: { resultado.get('cpf')}
        Carteira: {resultado.get('carteira')}
    ''')
main()
