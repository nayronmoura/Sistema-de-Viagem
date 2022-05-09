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


