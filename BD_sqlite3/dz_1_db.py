import sqlite3
conn = sqlite3.connect('book.db')
cursor = conn.cursor()
# Создадим таблицу с тремя текстовыми колонками, кол_1 и кол_2 это колонки. таб_1 имя таблицы.
# Айди присваивается по порядку с таким кодом id Integer primary...
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50), author VARCHAR(30), price DECIMAL(8,2), amount INT) ''')
cursor.execute('''INSERT into tab_1(title, author, price, amount) VALUES('Война и мир','Лев Толстой', (124,89), 55)''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
