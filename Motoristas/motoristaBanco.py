import json

banco = json.load(open("bancomotorista.txt", 'r'))


def pegar(cpf):
    with open("bancomotorista.txt", 'r') as fp:
        value = json.load(fp)


def checkCPF(cpf):
    if cpf == banco.get(cpf):
        return True


def adicionar(motorista):
    try:
        banco = pegar()
        banco[motorista.get('cpf')] = motorista
        with open("bancomotorista.txt", 'w') as fp:
            json.dump(dict(banco), fp, indent=4)
    except:
        print("Houve um erro no cadastro, tente novamente.")


banco = pegar('')
