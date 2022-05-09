import Menus
import veiculoBanco
banco = veiculoBanco

def main():
    Menus.menu_veiculo()
    chose = int(input(" Escolha uma opção: "))
    match chose:
        case 1:
            cadastrar()
        case 2:
            buscarPlaca()
        case 3:
            motoristaVeiculo()




def cadastrar():
    while True:
        placa = str(input('Digite a placa que quer cadastrar: '))
        if banco.checkPlaca(placa):
            print('A placa já está cadastrada!! ')
        else:
            break
    while True:
        tipo = str(input('é: [1] Carro    [2] Moto'))
        if tipo == 2:
            veiculo = 'moto'
        elif tipo == 1:
            veiculo = 'carro'
        else:
            break


def motorista():
    while True:
        motorista = str(input('Digite o nome do Motorista; '))
        if banco.checkMotorista(motorista):
            print('O motorista já está cadastrado!!')
        else:
            break

def buscarPlaca():
    while True:
        placa = str(input('Digite a placa que deseja encontrar: '))
        if banco.checkPlaca(placa):
            print('Informações da placa cadastrada:', motorista, veiculo)
        else:
            break

def motoristaVeiculo():
    while True:
        placa = str(input('digite a placa: '))
        motorista = str(input('Digite o motorista que quer adicionar a placa: '))




main()