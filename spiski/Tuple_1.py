#Задача№1
#Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму
#Задача№2
#Выведите статистику частности букв в кортеже
#Примечание: Статистика частности - число повторений каждой из букв.
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
import random
f = [random.randint(0,9) for i in range(10)]
print(f)
print('Задача 1.', sum(f))
a = 0
b = 0
c = 0
for i in long_word:
    if i=='т':
        b = b + 1
    elif i=='а':
        a = a + 1
    else:
        c = c + 1
print('Задача 2.')
print('Букв т в кортеже - ', b)
print('Букв а в кортеже - ', a)
print('Букв и в кортеже - ', c)
