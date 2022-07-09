import sqlite3
conn = sqlite3.connect('domZ.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(ID INTEGER PRIMARY KEY AUTOINCREMENT,
text_1 VARCHAR(30)) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT,
cifr_1 INTEGER) ''')
conn.commit()
spis = [1,2, 'holiday', 'привет', 'world', 3, 4, 5]
for i in spis:
    if type(i) is int:
        if i%2 == 0:
            cursor.execute('''INSERT into tab_2(cifr_1) VALUES (?)''', (i,))
            conn.commit()
        else:
            cursor.execute('''INSERT into tab_1(text_1) VALUES ('нечетное')''')
            conn.commit()
    else:
        n = len(i)
        cursor.execute('''INSERT into tab_1(text_1) VALUES (?)''', (i,))
        cursor.execute('''INSERT into tab_2(cifr_1) VALUES (?)''', (n,))
        conn.commit()
z = 0# количество в первой таблице
x = 0#  во второй
for j in cursor.execute('''SELECT * FROM tab_1'''):
    z += 1
for o in cursor.execute('''SELECT * FROM tab_2'''):
    x += 1
if x>5:
    cursor.execute('''DELETE FROM tab_1 WHERE id=1''')
else:
    cursor.execute('''UPDATE tab_1 SET text_1 = ('hello') WHERE id=1''')

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.execute('''SELECT*FROM tab_2''')
l = cursor.fetchall()
print(l)