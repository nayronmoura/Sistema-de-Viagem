import json


def atualizaBanco():
    dados = {}
    with open('../Viagem/bancoViagem.json', 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarViagem(placa):
    banco = atualizaBanco()
    return banco.get(placa)


def vefificaViagem(placa):
    banco = atualizaBanco()
    if placa in banco:
        veiculo = banco.get(placa)
        if veiculo.get('status'):
            return True
        else:
            return False
    else:
        return False


def cadastrar(viagem):
    banco = atualizaBanco()
    banco[viagem.get('placa')] = viagem
    with open('../Viagem/bancoViagem.json', 'w') as fp:
        json.dump(dict(banco), fp, indent=4)
