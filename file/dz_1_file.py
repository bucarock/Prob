# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел.
# Вывести в файл ‘output.txt’ их разность
a=['5','7']
f = open("input.txt",'w')
f.write(a[0] + ' '+ a[1])
f.close()

f1 = open("output.txt", 'w')
b=int(a[1])-int(a[0])
f1.write(str(b))
f1.close()
f1 = open("output.txt", 'r')
print(f1.readline())
