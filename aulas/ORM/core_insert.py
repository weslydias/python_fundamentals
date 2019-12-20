from core import user_table, engine


con = engine.connect()
ins = user_table.insert()

# Insert Pessoa
def insert_unico():
    new = ins.values(idade=24, nome='teste', senha='testanto')
    con.execute(new)

# Insert Pessoas
def insert_multiplo():
    con.execute(ins,[
        {'nome':'marcio', 'idade':20, 'senha':'senha123'},
        {'nome':'gustavo', 'idade':18, 'senha': 'abacaxi123'},
        {'nome':'guilherme', 'idade':22, 'senha':'goiaba123'}

    ])


if __name__ == "__main__":
    # insert_unico()
    insert_multiplo()