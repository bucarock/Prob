import sqlite3
conn = sqlite3.connect('baza1.db')
cursor = conn.cursor()
# Создадим таблицу с тремя текстовыми колонками, кол_1 и кол_2 это колонки. таб_1 имя таблицы.
# Айди присваивается по порядку с таким кодом id Integer primary...
a = int(input())
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT, col_3 INTEGER) ''')
cursor.execute('''INSERT into tab_1(col_1,col_2,col_3) VALUES('hello','world',?)''',(a,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    i = list(i)#Преобразовали к списку.
    h = 0
    print(' '.join(str(h) for h in i))# с помощью джоин и фор внутри джоин, перебрали список. ( так как разные типы данных)