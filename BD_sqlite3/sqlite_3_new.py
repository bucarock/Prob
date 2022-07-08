import sqlite3   #Сначала нужно импортировать СКюлайт3

# Создаём Базу данных.    Конн - это имя базы данных. Сами выбираем.
conn = sqlite3.connect('name1.db')  # найм это имя файла и таблицы
# Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками, кол_1 и кол_2 это колонки. таб_1 имя таблицы.
# Айди присваивается по порядку с таким кодом id Integer primary...
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')

# Заполняем таблицу данными
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
# Сохраняем изменения. обязательно это нужно сохранять.
conn.commit()

# d = "red"
# f = "black"
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
# cursor.execute('''INSERT INTO tab_2(col_1,col_2) VALUES (?,?)''', (d, f))
# conn.commit()

cursor.execute('''SELECT*FROM tab_1''') # Если select* - то всю таблицу. Если кол_1 то только 1 колонку.
k = cursor.fetchall()
print(k)