# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за
# контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать
# средний балл по классу.
a = open('klass.txt', 'w')
a.write('alesha Popovich - 2'+'\n')
a.write('dobrinya Nikitich - 3'+'\n')
a.write('iliya Myrometc - 5'+'\n')
a.write('Solovey Razboinik - 2'+'\n')
a.write('Gai Yuliy - 4'+'\n')
a.write('Zmei Gorinych - 2'+'\n')
a.close()
b = 0#сумма
c = 0# кол-во
with open('klass.txt', 'r') as a:
    for i in a:
        g = int(i[-2])
        b += g
        c += 1
        if g<3:
            print(i)
        else:
            continue
print('Средний балл в классе = ', b/c)
