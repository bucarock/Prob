#Даны 2 списка:
#Тебе нужно выполнить следующие операции:
#1. Сложить два списка
#2. Добавить элемент 6 на 3 позицию.
#3. Посчитать сколько раз встречается число 6
#4. Посчитать количество элементов списка
#5. Вывести 1 элемент вложенного списка
a = [4,6,'pу','tell',78]
b = [44,'hello',56,'exept',['world',5.7],3,6]
f = a+b
c = []
print('1-', f)
c.extend(a)
c.extend(b)
print('1.1 Метод второй-', c)
a.insert(3,6)
d = a
print('2-', d)
print('3 Список а-', a.count(6))
print('3.1 Список b-', b.count(6))
print('4.1-', len(a))
print('4.2-', len(b))
print('5-', b[4][1])

