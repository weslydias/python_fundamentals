#!/usr/bin/python3
# -*- coding: utf-8 -*-

# def printa_nome(nome):
#     print(nome)

# printa_nome("Wesly")

def sum(n1, n2):
    return (n1+n2)

def sub(n1, n2):
    return (n1-n2)

def div(n1, n2):
    if (n2==0):
        print('Erro, não se pode dividr por 0')
    else:
        return (n1/n2)

def mult(n1, n2):
    return (n1*n2)

print('1 - Somar')
print('2 - Subtrair')
print('3 - Dividir')
print('4 - Multiplicar')
op = int(input('Escolha a opção desejada: '))
n1 = int(input('Informe o numero 1: '))
n2 = int(input('Informe o numero 2: '))

if (op==1):
    print(f'A soma é {sum(n1, n2)}')
elif (op==2):
    print(f'A subtração é {sub(n1, n2)}')
elif (op==3):
    print(f'A divisão é {div(n1, n2)}')
elif (op==4):
    print(f'A multiplicação é {mult(n1, n2)}')
else:
    print('Opção errada!')


