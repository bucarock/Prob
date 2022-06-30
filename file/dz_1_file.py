# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность

f = open("input.txt",'w')
f.write('7 5')
f.close()
f = open("input.txt",'r')
d = 0
c = int()
r = int()
c = int(f.read(1))
print(c)
r = int(f.read(3))
print(r)
d = int(c - r)
u = open("output.txt",'w')
u.write(d)
u.close()
print(u.readlines())
