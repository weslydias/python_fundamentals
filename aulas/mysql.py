import MySQLdb

try:
    con = MySQLdb.connect(host="localhost", user="admin", passwd="4linux", db="projetos")
    cur = con.cursor()
    cur.execute("insert into clientes(nome, endereco) values ('Carlos', 'Wesly')")
    con.commit()
    print("Registro criado com sucesso!")
except Exception as e:
    print(f'Erro: {e}')
    print('Fazendo Rollback...')
    con.rollback()
finally:
    print('Finalizando conexão com o banco de dados...')
    cur.close()
    con.close()