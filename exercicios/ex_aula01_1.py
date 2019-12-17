#!/usr/bin/python3

# dada a string:

# Não deixe o barulho da opinião dos outros abafar sua voz interior.
# E mais importante, tenha a coragem de seguir seu coração e sua intuição.
# Eles de alguma forma já sabem o que você realmente quer se tornar.
# Tudo o mais é secundário.

texto = "Não deixe o barulho da opinião dos outros abafar sua voz interior. \
E mais importante, tenha a coragem de seguir seu coração e sua intuição. \
Eles de alguma forma já sabem o que você realmente quer se tornar. \
Tudo o mais é secundário."

# conte quantas letras a tem no texto

print("Texto: ", texto)
print()
print("O texto tem", len(texto), "letras")
print()
print("O texto tem", texto.count('a'), "letras a")
print()

# mude todas as letras o para s

print(texto.replace('o', 's'))
print()

# divida o texto em uma lista colocando virgulas nos espaços

print(texto.split(' '))
