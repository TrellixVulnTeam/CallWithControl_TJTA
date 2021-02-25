import sqlite3
conn = sqlite3.connect(r'D:\sqlite\teste.db')
cursor = conn.cursor()
cont = []
cursor.execute("""SELECT * FROM ticket""")
for c in cursor.fetchall():
    cont.append(c[0])

print(len(cont))

id = len(cont) + 1
print(id)






'''
id = 1
linha = 'ENN1 - L1'
area = 'MANUTENÇÃO'
databr = '31/1/2021'
hora = '10:30:00'
usuario = 'Guilherme Vargas'
tupla = (linha,area,databr,hora,usuario)



#sqlite_insert_with_param = """INSERT INTO ticket1 (linha, area, data, hora, usuario) VALUES (?, ?, ?, ?, ?);"""


#cursor.execute(sqlite_insert_with_param, tupla)




cursor.execute("""
UPDATE ticket
SET status = ?
WHERE id = ?""",('Aberto',1))
conn.commit()
cursor.close()


class teste():

    def horadata(self):
        from datetime import date
        from datetime import datetime
        hora = str(datetime.now())
        hora = hora[11:19]
        data = date.today()
        databr = f'{data.day}/{data.month}/{data.year}'
        return databr,hora
'''


