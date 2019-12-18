#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Crie uma classe automovel, com os atributos: motor, marca, preco, ano
# e com os metodos que retornam valor de: motor, marca, anp e preco

# class Automovel():

#     def __init__(self):
#         self.motor = 1.0
#         self.marca = 'Qualquer'
#         self.preco = 0
#         self.ano = 0000

#     def infMotor(self, motor):
#         self.motor = motor

#     def infMarca(self, marca):
#         self.marca = marca

#     def infPreco(self, preco):
#         self.preco = preco

#     def infAno(self, ano):
#         self.ano = ano

# carro = Automovel()
# moto = Automovel()

# op = int(input('Escolha 1 para Carro e 2 para Moto: '))
# if op == 1:
#     carro.infMotor(input('Informe o motor: '))
#     carro.infMarca(input('Informe a marca: '))
#     carro.infPreco(input('Informe o preço: '))
#     carro.infAno(int(input('Informe o ano')))

#     print('Informações do seu carro:')
#     print(f'Motor: {carro.motor}')
#     print(f'Marca: {carro.marca}')
#     print(f'Preço: {carro.preco}')
#     print(f'Ano: {carro.ano}')

# else:
#     moto.infMotor(input('Informe o motor: '))
#     moto.infMarca(input('Informe a marca: '))
#     moto.infPreco(input('Informe o preço: '))
#     moto.infAno(int(input('Informe o ano: ')))

#     print('Informações da sua moto:')
#     print(f'Motor: {moto.motor}')
#     print(f'Marca: {moto.marca}')
#     print(f'Preço: {moto.preco}')
#     print(f'Ano: {moto.ano}')

# ====================================================================================

# Faça uma classe de uma conta bancaria que tera os seguintes
# atributos:
            # Nome do banco  Oldbak
#            Número do banco    99
            # Número da agencia
            # número da conta
            # nome do cliente
            # saldo


# métodos:
#         Sacar
#         Depositar
#         Extrato


# Menu

# 1 - para saque
# 2 - deposito
# 3 - extrato


# Extrato

# Nome do Banco
# ====================
# Clinte: tal
# Conta: tal Ag: ta
#  Saldo

class Banco():

    def __init__(self, ag, conta, cliente, saldo, nome_banco='Oldbak', num_banco=99):
        self.ag = ag
        self.conta = conta
        self.cliente = cliente
        self.saldo = saldo

    def sacar(self, saldo):
        self.saldo -= saldo
        print(f'O novo saldo é de R$ {self.saldo}')

    def depositar(sefl, saldo):
        self.saldo += saldo

    def extrato(self):
        print('Extrato simplificado')
        print('=======================')
        print(f'Banco {self.nome_banco}')
        print('=======================')
        print(f'Clinte {self.cliente}')
        print(f'Conta: {self.conta}    Agência: {self.agencia}')
        print(f'Saldo: {self.saldo}')


# Menu
# banco = Banco()

# print('Escolha uma das opções abaixo:')
# print('1 - Sacar')
# print('2 - Depositar')
# print('3 - Extrato')
# op = int(input('Opção escolhida: ')

# if (op == 1):
#     saldo=int(input('Digite o valor a ser sacado: '))
#     banco.sacar(saldo)
# else:
#     print('Acabou')
