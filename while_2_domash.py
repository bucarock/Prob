#Пользователь вводит два числа с клавиатуры, необходимо вывести на экран все отрицательные числа,
# лежащие между ними. Например, пользователь ввел -5 и 3, на экране вывелось -4,-3,-2,-1
a = int(input('Введите отрицательное число - '))
b = int(input('Введите второе положительное число - '))
while a<0:
    print(a)
    a = a + 1
else:
    print('Конец')