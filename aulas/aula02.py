# #!/usr/bin/python3
# # Revisão

# # Entrada e saida de dados

# nome = input('Digite seu nome: ')
# print(f'O nome digitado foi {nome}')

# # Revisão
# import os
# # var = os.getenv('SSH_AUTH_SOCK')


# # Entrada e sáida de dados

# # Entrada: input()
# # Saída: Print()

# # nome = input('Digite seu nome: ')

# # print(f'O nome digitado foi {nome}')

# # Repetição

# # item for item in range(10):
# #     print(item)

# # numeros = [1, 2, 3, 4, 5, 6]
# # multiplicado = [i*15 for i in numeros]

# # print(multiplicado)

# # lst = []

# # for letra in 'abcd':
# #     for num in range(4):
# #         lst.append((letra, num))

# # print(lst)

# # Dicionarios


# # dicionario = {'chave': {'chave02': 'Valor'

# #                         }

# #               }


# # const  = dict(chave1='valor1', chave2='valor2')

# # print(const)


# # tuplas

# # imutavel = (1, 2, 3, 1, 1, 1, 1)
# # print(imutavel.count(1))


# # Erros e Exceções


# # try:
# #     x = int(input('Digite o primeiro numero: '))
# #     y = int(input('Digite o segundo numero: '))
# #     print(x + y)

# # except ValueError as e:
# #     print('Valor Incorreto')

# # finally:
# #     print('Sando do ')


# ## Error Types


# # NameError

# # try:
# #     print(f'A Linguagem é {liguagem}')

# # except NameError as e:
# #     print('Esse é um NameError', e)


# # TypeError

# # try:
# #     numero = 10
# #     print('O numero é: ' + 10)
# # except TypeError as t:
# #     print(f'Esse é um TypeError: ({t})')


# # print('teste'+ 10)

# # IndexError

# # try:
# #     liguagem = ['python']
# #     print(f'A linguagem é: {liguagem[2]}')

# # except IndexError as i:
# #     print(f'Esse é um IndexError: ({i})')


# # KeyError

# # try:
# #     linguagem = {'curso': 'fundamentals'}
# #     print(f'A linguagem é: {linguagem["name"]}')

# # except SyntaxError as s:
# #     print(f'Esse é um SyntaxError: {s}')

# # except KeyError as e:
# #     print(f'Esse é um KeyError: ({e})')

# ## Raise Exception
# # 104

# # while True:
# #     try:
# #         senhas = [3030, 3242, 3333, 1240]
# #         senha_usuario = int(input('Digite sua senha: '))
# #         if senha_usuario not in senhas:
# #             raise NameError('Senha invalida, tente novamente! ')
# #             continue
# #         else:
# #             print('Login efetuado!')
# #             break
# #     except NameError as n:
# #         print(n)


# print('Bem vindo ao Banco T!')
# print('Escolha uma oção abaixo:')
# print('Digite 1 para saque')
# print('Digite 2 para deposito')
# print('Digite 9 para sair')
# opcao = int(input('>>> '))

# while True:
#     opcao = int(input('>>> '))
#     if opcao == 1:
#         print('Saque selecionado!')
#         break
#     elif opcao == 2:
#         print('Deposito selecionado!')
#         break
#     elif opcao == 9:
#         print('Obrigado, volte sempre!')
#         break
#     else:
#         print('Opção Inválida')
#         continue

#manipulação de arquivos
with open('arquivo.txt') as p:
    p.write('Curso Python ')