import menus
import veiculoBanco

banco = veiculoBanco


def main():
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
    while True:
        placa = str(input('Digite a placa que quer cadastrar: '))
        if banco.checkPlaca(placa):
            print('A placa já está cadastrada!! ')
        else:
            break
    while True:
        tipo = int(input('é: [1] Carro    [2] Moto'))
        if tipo == 2:
            veiculo = 'moto'
            break
        elif tipo == 1:
            veiculo = 'carro'
            break
        else:
            print('O valor não é válido !!')
    banco.cadastro({'placa': placa, 'tipo': veiculo, 'motorista': ''})
    main()


def motorista():
    while True:
        motorista = str(input('Digite o nome do Motorista; '))
        if banco.checkMotorista(motorista):
            print('O motorista já está cadastrado!!')
        else:
            break
    main()


def buscarPlaca():
    while True:
        placa = str(input('Digite a placa que deseja encontrar: '))
        if banco.checkPlaca(placa):
            veiculo = banco.buscarPlaca(placa)
            print(f'''
            PLACA: {veiculo.get('placa')}
            MOTORISTA: {veiculo.get('motorista')}
            TIPO: {veiculo.get('tipo')}
            ''')
        else:
            break
    main()


def motoristaVeiculo():
    while True:
        placa = str(input('digite a placa: '))
        if banco.checkPlaca(placa):
            motorista = str(input('Digite o motorista que quer adicionar a placa: '))
            banco.motoristaVeiculo(placa, motorista)
            break
        else:
            print('Digite A placa corretamente !!')
    main()


def removerMotorista():
    while True:
        placa = str(input('digite a placa: '))
        if banco.checkPlaca(placa):
            banco.removerMotorista(placa)
            break
        else:
            print('Digite A placa corretamente !!')
    main()


def veiculosEmotoristas():
    veiculos = banco.bancoveiculo()
    for a in veiculos.values():
        if a.get('motorista') != '':
            print(f'''
                Placa: {a.get('placa')}
                motorista: {a.get('motorista')}
                Tipo: {a.get('tipo')}
            ''')
    main()


def motoristasSveiculos():
    veiculos = banco.bancoveiculo()
    for a in veiculos.values():
        if a.get('motorista') != '':
            print(f'''
                    placa:{a.get('placa')}
                    tipo:{a.get('tipo')}
                ''')
    main()


def removerVeiculo():
    while True:
        placa = str(input('digite a placa: '))
        if banco.checkPlaca(placa):
            banco.removerVeiculo(placa)
            break
        else:
            print('Digite A placa corretamente !!')
    main()


main()
