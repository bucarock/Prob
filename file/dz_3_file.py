# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.
import os

f = open("1.txt", 'r')
print(f.readlines())
print('Количество строк в файле = ', sum(1 for line in open("1.txt", 'r')))
n = 0
f = open("1.txt", 'r')
for i in f:
    n = n + 1
    print(f' В {n} строке количество символов - ' , len(i)-1)
f.close()
