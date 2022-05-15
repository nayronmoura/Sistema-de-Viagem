import re

import menus
from Veiculo import veiculoBanco

banco = veiculoBanco
regex = re.compile(r"[A-Z]{3}[0-9][0-9A-Z][0-9]{2}")


def main():
    print(" \n ")
    menus.menuVeiculo()
    chose = int(input("Escolha uma opção: "))
    match chose:
        case 1:
            cadastrar()
        case 2:
            buscarPlaca()
        case 3:
            motoristaVeiculo()
        case 4:
            removerMotorista()
        case 5:
            veiculosEmotoristas()
        case 6:
            motoristasSveiculos()
        case 7:
            removerVeiculo()


def cadastrar():
    print("-" * 30)
    while True:
        print("A placa deve seguir o padrão AAA0A00.")
        placa = str(input('Digite a placa que quer cadastrar: '))
        if regex.match(placa):
            if banco.checkPlaca(placa):
                print('A placa já está cadastrada!! ')
            else:
                break
        else:
            print("Placa digitada incorretamente.")
    while True:
        tipo = int(input('é: [1] Carro \n  [2] Moto\n:  '))
        if tipo == 2:
            veiculo = 'moto'
            break
        elif tipo == 1:
            veiculo = 'carro'
            break
        else:
            print('O valor não é válido !!')

    banco.cadastro({'placa': placa, 'tipo': veiculo, 'motorista': ''})
    print("-" * 30)
    main()


def buscarPlaca():
    print("-" * 30)
    while True:
        placa = str(input('Digite a placa que deseja encontrar: '))
        if regex.match(placa):
            if banco.checkPlaca(placa):
                veiculo = banco.buscarPlaca(placa)
                print(f'''
                PLACA: {veiculo.get('placa')}
                MOTORISTA: {veiculo.get('motorista')}
                TIPO: {veiculo.get('tipo')}
                ''')
                print("-" * 30)
                break
            else:
                print("placa não encontrada")
        else:
            print("Placa digitada incorretamente.")
    main()


def motoristaVeiculo():
    print("-" * 30)
    while True:
        placa = str(input('digite a placa: '))
        if regex.match(placa):
            if banco.checkPlaca(placa):
                motorista = str(input('Digite o motorista que quer adicionar a placa: '))
                banco.motoristaVeiculo(placa, motorista)
                print("-" * 30)
                break
            else:
                print('Digite A placa corretamente !!')
        else:
            print("Placa digitada incorretamente.")
    main()


def removerMotorista():
    print("-" * 30)
    while True:
        placa = str(input('digite a placa: '))
        if regex.match(placa):
            if banco.checkPlaca(placa):
                banco.removerMotorista(placa)
                print("-" * 30)
                break
            else:
                print('Digite A placa corretamente !!')
        else:
            print("Placa digitada incorretamente.")
    main()


def veiculosEmotoristas():
    veiculos = banco.bancoveiculo()
    if len(veiculos)>0:
        index = 0
        for a in veiculos.values():
            if a.get('motorista') != '':
                index+=1
                print(f'''
                    Placa: {a.get('placa')}
                    motorista: {a.get('motorista')}
                    Tipo: {a.get('tipo')}''')
        if index == 0:
            print("Não há veículos com motorista.")
        print("-" * 30)
    else:
        print("Não há veículos cadastrados.")

    main()


def motoristasSveiculos():
    veiculos = banco.bancoveiculo()
    if len(veiculos) > 0:
        index = 0
        for a in veiculos.values():
            if a.get('motorista') == '':
                index+=1
                print(f'''
                        placa:{a.get('placa')}
                        tipo:{a.get('tipo')}''')
        if index == 0:
            print("Não há veículos sem motorista.")
        print("-" * 30)
    else:
        print("Não há veículos cadastrados.")
    main()


def removerVeiculo():
    while True:
        placa = str(input('digite a placa: '))
        if banco.checkPlaca(placa):
            banco.removerVeiculo(placa)
            print("-" * 30)
            break
        else:
            print('Digite A placa corretamente !!')
    main()
