from pymongo import MongoClient

# client = MongoClient('localhost')
# db = client['dexterops']


# def inserir_dados():
#     try:
#         db.fila.insert({"_id": 10, "empresa": "dexterops",
#                         "produtos": [{
#                             "produto01": "camiseta batman preta",
#                             "produto02": "camiseta homem aranha",
#                             "produto03": "camiseta demolidor",
#                             "produto04": "camiseta justiceiro preta"
#                         }]})

#     except Exception as e:
#         print(f'Erro: {e}')


# if __name__ == "__main__":
#     inserir_dados()

from pymongo import MongoClient
client = MongoClient('localhost')
db = client['dexterops']

def inserir_dados():

    try:
        db.fila.insert({
            "_id":12, 
            "empresa": "xpto", 
            "produtos": [{"produto":"camiseta Homem Aranha",
                            "preco": 49.90},
                            {"produto":"camiseta Hulk",
                            "preco": 19.90},
                            {"produto":"caneca Homem de ferro",
                            "preco": 89.90}
                            
                        ]
                    })


    except Exception as e:
        print(f'Erro:{e}')
        

def buscar_dados():

    for empresas in db.fila.find():
        print('Empresa: {}'.format(empresas['empresa']))
        for produto in empresas['produtos']:
            print('===============')
            print('Produto: {} \nPreço: {}'.format(produto['produto'], produto['preco']))



def adicionar_produto():
    db.fila.update({"_id":12}, {"$addToSet":
                                {"produtos":{'produto': 'Camiseta Ricky and morty',
                                             'preco': 99.9}}
                                             })

def atualiza_preco():
    # id = int(input('Digite o número do id: '))
    db.fila.update({"_id":11, "produtos.preco": 19.9},
                    {"$set":{"produtos.$.preco": 39.9}})


if __name__ == "__main__":
    # inserir_dados()
    # buscar_dados()
    # atualiza_item()
    adicionar_produto()
    buscar_dados()












