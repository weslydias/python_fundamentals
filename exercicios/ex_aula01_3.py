#!/usr/bin/python3

dados = {

    'cidades': {
        'saopaulo': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 12.18
        },
        'riodejaneiro': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 6.32
        },
        'minasgerais': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87

        }
    }
}

# imprima a quantiddade de municipios de minas

print("Municipios MG: ", dados['cidades']['minasgerais']['municipios'])

# imprima a quantidade de municipios do rio

print("Municipios RJ: ", dados['cidades']['riodejaneiro']['municipios'])

# imprima o nome e população de são paulo em milhoes

print('Cidade: ', dados['cidades']['saopaulo']['nome'],
      "  População: ", dados['cidades']['saopaulo']['população'])
