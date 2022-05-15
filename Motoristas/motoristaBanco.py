import json


def atualizaBanco():
    with open("./Motoristas/bancomotorista.json", 'r') as fp:
        dados = json.load(fp)
    return dados


def pegarCPF(cpf):
    with open("./Motoristas/bancomotorista.json", 'r') as fp:
        dados = json.load(fp)
    return dados.get(cpf)


def checkCPF(cpf):
    banco = atualizaBanco()
    if cpf in banco:
        return True


def adicionar(motorista):
    try:
        banco = atualizaBanco()
        banco[motorista.get('cpf')] = motorista
        with open("./Motoristas/bancomotorista.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


def altera(cpf, nome):
    try:
        banco = atualizaBanco()
        motorista = banco.get(str(cpf))
        motorista['nome'] = nome
        banco[cpf] = motorista
        with open("./Motoristas/bancomotorista.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
        return f"O Motorista do CPF {cpf} foi alterado com sucesso"
    except:
        print("Ocorreu um erro ao tentar alterar, tente novamente.")


def remover(cpf):
    try:
        banco = atualizaBanco()
        banco.pop(cpf)
        with open("./Motoristas/bancomotorista.json", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Ocorreu um erro, tente novamente.")


def pegarTodos():
    banco = atualizaBanco()
    return banco.values()
