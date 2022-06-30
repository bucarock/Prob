print('Добро поаловать в сумму значений вашего числа')
abc = int(input('Введите трехзначное число - '))
a = abc % 10
#print(a)
abc = abc // 10
#print (abc)
b = abc % 10
#print(b)
abc = abc // 10
#print(abc)


print("Сумма цифр вашего числа равна",abc+a+b)