import json


def bancoveiculo():
    with open('./Veiculo/bancoveiculo.json', 'r') as fp:
        dados = json.load(fp)
        return dados


def checkPlaca(placa):
    banco = bancoveiculo()
    if placa in banco:
        return True


def cadastro(veiculo):
    banco = bancoveiculo()
    banco[veiculo.get('placa')] = veiculo
    with open('./Veiculo/bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)


def buscarPlaca(placa):
    banco = bancoveiculo()
    return banco.get(placa)


def motoristaVeiculo(placa, motorista):
    banco = bancoveiculo()
    veiculo = banco.get(placa)
    veiculo['motorista'] = motorista
    banco[placa] = veiculo
    with open('./Veiculo/bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)


def removerMotorista(placa):
    banco = bancoveiculo()
    veiculo = banco.get(placa)
    veiculo['motorista'] = ''
    banco[placa] = veiculo
    with open('./Veiculo/bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)


def removerVeiculo(placa):
    banco = bancoveiculo()
    banco.pop(placa)
    with open('./Veiculo/bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)
