#!/usr/bin/python3

# Crie um programa que peça um numero e multiplique por 15

#num = int(input('Digite um número: '))
# print(
#    f'O número digitado foi {num} e multiplicado por 15 é igual a {(num * 15)}')


# Repetição
# Multiplique os números da lista numeros por 15
# e coloque o resultado na lista multiplicados

# numeros = [1, 2, 3, 4, 5, 6]
# multiplicados = []

# for numero in numeros:
#     multiplicados.append(numero * 15)
# print(multiplicados)

# ou

# numeros = [1, 2, 3, 4, 5, 6]
# multiplicado = [i*15 for i in numeros]
# print(multiplicado)

#ou

# multiplicado = [i*15 for i in range(1, 7)]
# print(multiplicado)

#-----------------------------------------------------------------------
#Erros e Exceções
# Try e Except
# 
# fazer um sistema que pergunte o sexo do usuario sendo M, F
# mostre se o usuário é do sexo masculino ou feminino

# sex = input('Qual seu sexo? (M ou F) ')
# if (sex == 'M'):
#     print('Usuario do sexo masculino.')
# elif (sex == 'F'):
#     print('Usuário do sexo feminino.')
# else:
#     print('Sexo informado errado!')

# print('Digite seu sexo')
# print('M - para Masculino')
# print('F - para Feminino')

# while True:
#     user = input('>>> ')
#      if user.lower() == 'm':
#         print('Usuario de sexo masculino')
#         break
#     elif user.lower() == 'f':
#         print('Usuario do sexo feminino')
#         break
#     else:
#         print('Entrada Invalida, Digite novamente! ')
#         continue

# usuarios = ['ana', 'bruno', 'caio', 'camila', 'joao']

#peça para o usuário digitar o eu nome  e caso não esteja na lista
#print um erro "Usuario não cadastrado!"

# try:
#     login = input('Digite seu login: ')
#     if login.lower() not in usuarios:
#         raise NameError('Usuário não cadastrado!')
#     else:
#         print(f'Bem vindo, {login}')

# except NameError as n:
#     print(n)