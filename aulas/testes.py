# def soma (x, y):
#     return x + y

# def subtrair(x, y):
#     return x - y

# def multiplicar(x, y):
#     return x * y

# def dividir(x, y):
#     return x/y


# assert soma(2, 2) == 4, f"Obtido: {soma(2, 2)}, Esperado: 4"
# assert subtrair(2, 2) == 0, f"Obtido: {subtrair(2, 2)}, Esperado: 0"
# assert multiplicar(2, 3) == 6, f"Obtido: {multiplicar(2, 3)}, Esperado: 6"
# assert dividir(16, 2) == 7, f"Obtido: {dividir(16, 2)}, Esperado: 8"

def maior(*valores):
    return max(valores)


assert maior(12, 45, 88, 96, 109, 111, 13, 0, 89, 999) == 999, f'Obtido: \
    {maior(12, 45, 88, 96, 109, 111, 13, 0, 89, 999)}, Esperado: 999'
