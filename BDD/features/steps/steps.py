from behave import step

def soma (x, y) -> int:
    return x+y

@step('somar "{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))

@step('O resultado de ser "{esperado}"')
def teste_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "descrição do erro"