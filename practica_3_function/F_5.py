# Написать функцию, которая
# определяет
# количество
# разрядов
# введенного
# целого
# числа


def digit(n):
    i = 0
    while n>0:
        n = n//10
        i+=1
    return i

print(digit(1235564))