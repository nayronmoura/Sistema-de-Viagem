<<<<<<< HEAD
import json


def bancoveiculo():
    with open('bancoveiculo.json', 'r') as fp:
        dados = json.load(fp)
        return dados


def checkPlaca(placa):
    banco = bancoveiculo()
    if placa in banco:
        return True


def cadastro(veiculo):
    banco = bancoveiculo()
    banco[veiculo.get('placa')] = veiculo
    with open('bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)


def buscarPlaca(placa):
    banco = bancoveiculo()
    return banco.get(placa)

def motoristaVeiculo(placa,motorista):
    banco = bancoveiculo()
    veiculo = banco.get(placa)
    veiculo['motorista'] = motorista
    banco[placa] = veiculo
    with open('bancoveiculo.json', 'w') as fp:
        json.dump(dict(banco),fp, indent=4)


def removerMotorista(placa):
    banco = bancoveiculo()
    veiculo = banco.get(placa)
    veiculo['motorista'] = ''
    banco[placa] = veiculo
    with open('bancoveiculo.json','w') as fp:
        json.dump(dict(banco),fp, indent=4)


def removerVeiculo(placa):
    banco = bancoveiculo()
    banco.pop(placa)
    with open('bancoveiculo.json','w') as fp:
        json.dump(dict(banco),fp, indent=4)


=======
import json


def bancoveiculo():
    with open('bancoveiculo.json', 'r') as fp:
        dados = json.load(fp)
        return dados


def checkPlaca(placa):
    banco = bancoveiculo()
    if placa in banco:
        return True


 def cadastro():
     banco = bancoveiculo()
     banco[placa] =
     with open ('bancoveiculo.json', 'a') as fp:






def checkMotorista(motorista):
    banco = bancoveiculo()
    if motorista in banco:
        return True


def buscarPlaca(placa):
    banco = bancoveiculo()
    if placa in banco:
        return True


>>>>>>> 8a8063cdedaad4309bea0e1ffcacc058cf5bd1cf
