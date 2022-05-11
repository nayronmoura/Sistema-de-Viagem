import menus
import re
from datetime import date, datetime

import Veiculo.veiculoBanco as veiculoBanco
from Viagem import viagemBanco as banco

CPFexpr = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')  # expressão regular- É um padrão para strings


def main():
    menus.menuViagem()
    chose = int(input("Escolha uma opção: "))
    match chose:
        case 1:
            criarviagem()
        case 2:
            finalizarViagem()
        case 3:
            viagensAtivas()
        case 4:
            veiculosEmViagem()
        case 5:
            listarVeículos()
        case 6:
            listarViagens()
        case 7:
            listartPeriodo()


def criarviagem():
    while True:
        placa = str(input("insira a placa do veículo: "))
        if veiculoBanco.checkPlaca(placa):
            if not banco.vefificaViagem(placa):
                print(f'veículo {placa} selecionado.')
                rota = str(input("Qual a rota? ex: de Serra talhada para triúnfo   \n: "))
                banco.cadastrar({'placa': placa, 'rota': rota, 'data': f'{date.today()} -', 'status': True})
                break
            else:
                print('o Veículo atual já está em viagem')
        else:
            print('O veículo não está cadastrado.')


def finalizarViagem():
    while True:
        placa = str(input('Qual a placa do carro? '))
        if veiculoBanco.checkPlaca(placa):
            if banco.pegarViagem(placa):
                viagem = banco.pegarViagem(placa)
                banco.cadastrar({'placa': placa, 'rota': viagem.get('rota'),
                                 'data': (viagem.get('data') + f' {date.today()}'), 'status': False})
                print('viagem encerrada com sucesso.')
            else:
                print('O veículo não está em viagem')
        else:
            print('o veículo não está cadastrado')


def viagensAtivas():
    viagens = banco.atualizaBanco()
    counter = 0
    for viagem in viagens.values():
        if viagem.get('status'):
            counter += 1
            print(f'placa:{viagem.get("placa")}\n rota: {viagem.get("rota")}\n '
                  f'data: {viagem.get("data")}\n')
        if not counter > 1:
            print('não há viagens ativas.')


def veiculosEmViagem():
    veiculos = veiculoBanco.bancoveiculo()
    for veiculo in veiculos.values():
        if banco.vefificaViagem(veiculo.get('placa')):
            print(f'placa: {veiculo.get("placa")}\n tipo: {veiculo.get("tipo")}\n '
                  f'motorista:{veiculo.get("motorita")}')


def listarVeículos():
    veiculos = veiculoBanco.bancoveiculo()
    for veiculo in veiculos.values():
        if not banco.vefificaViagem(veiculo.get('placa')):
            print(f' placa: {veiculo.get("placa")}\n tipo: {veiculo.get("tipo")}\n '
                  f'motorista:{veiculo.get("motorita")}\n')


def listarViagens():
    viagens = banco.atualizaBanco()
    for viagem in viagens.values():
        print(f'placa: {viagem.get("placa")}\n rota: {viagem.get("rota")}\n '
              f'data: {viagem.get("data")} \n status: {viagem.get("status")}')


def listartPeriodo():
    viagens = banco.atualizaBanco()
    exp = re.compile('\d{4}\-\d{2}\-\d{2}')
    while True:
        print(f'formato da data: dia/mes/ano')
        print('data inicial')
        inicio = str(input("Insira a data inicial: "))
        if exp.match(inicio):
            inicio = toData(inicio)
            final = str(input("Insira a data final: "))
            if exp.match(final):
                final = toData(final)
                for viagem in viagens.values():
                    datas = str(viagem.get('data'))
                    if len(datas.split(' ')) == 3:
                        viagemFinal = toData(datas.split(' ')[2])
                        viagemInicial = toData(datas.split(' ')[0])
                        if viagemInicial >= inicio and viagemFinal <= final:
                            print(f'placa: {viagem.get("placa")}\n rota: {viagem.get("rota")}\n '
                                  f'data: {viagem.get("data")} \n status: {viagem.get("status")}')
                break
            else:
                print('data incorreta')
        else:
            print('data incorreta')

def toData(string):
    return datetime.strptime(string, '%Y-%m-%d').date()


main()
