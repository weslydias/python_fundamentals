from core import user_table, engine

con = engine.connect()
ins = user_table.insert()