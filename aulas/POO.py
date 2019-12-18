#!/usr/bin/python3
# -*- coding: utf-8 -*-

##POO Abstração

#entidades - Generalização
#atributos - Caracteristicas
#métodos - ações
#instãcias - Um exemplar de uma entidade

# class Passaro():
#     cont = 0
#     def __init__(self):
#         self.asas = 2
#         self.penas = True
#         self.bico = True
#         self.patas = 2
    
#     def voar(self):
#         if self.asas < 2:
#             print('Passaro com necessidades especiais!')
#             print('Não pode voar.')
#         else:
#             self.cont = 1
#             print('Voando...')
    
#     def pousar(self):
#         if self.cont == 0:
#             print('Passaro não está voando!')
#         else:
#             print('Pousando...')
    
#     def comer(self):
#         print('Comendo...')
    
#     def dormir(self):
#         print('Dormindo...')
    
#     def cantar(self):
#         print('Cantando...')

# canario = Passaro()
# canario.cantar()
# canario.asas = 1
# print(canario.asas)
# canario.pousar()

# class Servidor():

#     def __init__(self):
#         self.cpu = 2
#         self.memoria = 2048
#         self.disco = 500
    
#     def inserirCPU(self, cpu):
#         self.cpu += cpu

#     def inserirMEM(self, memoria):
#         self.memoria += memoria

#     def inserirDISCO(self, disco):
#         self.disco += disco
    
#     def removerCPU(self, cpu):
#         self.cpu -= cpu
    
#     def removerMEM(self, memoria):
#         self.memoria -= memoria

#     def removerrDISCO(self, disco):
#         self.disco -= disco

# servidorDNS = Servidor()
# #print(servidorDNS.memoria)
# #servidorDNS.inserirMEM(2048)
# #print(servidorDNS.memoria)

# # Crie uma classe automovel, com os atributos:
# #                             Motor
# #                             Marca
# #                             Ano
# #                             Preco

# # e com os métodos que retornam o valor de:
# #                                         Motor
# #                                         Marca
# #                                         Ano
# #                                         Preco


# class Automovel():

#     def __init__(self, motor, marca, ano, preco):
#         self.motor = motor
#         self.marca = marca
#         self.ano = ano
#         self.preco = preco

#     def get_motor(self):
#         print(self.motor)

#     def get_marca(self):
#         print(self.marca)

#     def set_marca(self, marca):
#         self.marca = marca

#     def get_ano(self):
#         print(self.ano)


#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, new_preco):
#         self._preco = new_preco
    
#     @preco.getter
#     def getpreco(self):
#         self._preco


# Crie uma classe automovel, com os atributos:
#                             Motor
#                             Marca
#                             Ano
#                             Preco

# e com os métodos que retornam o valor de:
#                                         Motor
#                                         Marca
#                                         Ano
#                                         Preco

"""
We are all consenting adults (algo como “somos todos adultos responsáveis”, 
significando que a linguagem não precisa ficar cercando o programador como se ele 
fosse criança)
"""



# class Automovel():

#     def __init__(self, motor, marca, ano, preco):
#         self.motor = motor
#         self.marca = marca
#         self.ano = ano
#         self.preco = preco

#     def get_motor(self):
#         print(self.motor)

#     def get_marca(self):
#         print(self.marca)

#     def get_ano(self):
#         print(self.ano)

#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, new_preco):
#         self._preco = new_preco
    

#     def get_preco(self):
#         print(self._preco)

# class Moto(Automovel):

#     def __init__(self, motor, marca, ano, preco, tipo='Moto'):
#         super().__init__(motor, marca, ano, preco)
#         self.rodas = 2

#     def ligar(self):
#         print('Ligada...')
    
#     def desligar(self):
#         print('Desligando...')
#         print( 'Desligada...')

#     def acelerar(self):
#         print('Acelerando...')
    
#     def frear(self):
#         print('Freando...')



# if __name__ == "__main__":
#     CB500 = Moto('500CC', 'Honda', 2017, 35000)
#     CB500.get_ano()
#     CB500.get_marca()
#     CB500.get_preco()
#     CB500.preco = 20000
#     CB500.get_preco()


# class Base():
#     def __init__(self):
#         print('Contrutor da classe Base')
    

# class Derivada(Base):
#     def __init__(self):
#         Base.__init__(self)
#         # super().__init__()
#         # print('Contrutor da classe Derivada')


# # base = Base()

# derivada = Derivada()



