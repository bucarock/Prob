f = open('1.txt', 'r')
s = f.readlines()
print(s)
a = []
b = []
for i in s:
    i = i[:-1]
    if i.isalpha():
        b.append(i)
    elif i.isdigit():
        i = int(i)
        a.append(i)
a.sort()
b.sort()
mas = a+b
print(mas)
f.close()

