import sqlite3 as sq
import json

data_base = 'PERSONAGENS.db'

conn = sq.connect(data_base)
cursor = conn.cursor()
# cursor.execute("insert into Characters (SupWep) values (?)",("{teste = [romantico,bruto,colorado]}",))
# conn.commit()
# cursor.execute('select SupWep from Characters where CharID=8')
# print(type(cursor.fetchall()[0]))
print(json.dumps({'teste':[1,2,3,4]}))
teste = json.loads('{"teste":[1,2,3,4]}')

print(teste['teste'])
