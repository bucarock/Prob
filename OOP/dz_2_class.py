# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или
# равно длине слова, выводить все гласные, иначе согласные; если число то, произведение
# суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе

class Example:
    def __init__(self):
        self.vvod()
    def raschet(self):
        result = self.dlina(self.a)
        if self.a.isdigit():
            for i in self.a:
                if int(i) % 2 == 0:
                    result = result * int(i)
            return result
        else:
            glas = ''
            soglas = ''
            for i in self.a:
                if i in 'аеёиоуыэюяeuoia':
                    glas = glas + i
                else:
                    soglas = soglas + i
            if self.dlina(soglas)*self.dlina(glas) > result or glas == '':
                return soglas
            else:
                return glas
    def dlina(self, b):
            return len(b)
    def vvod(self):
        self.a = input("Введите строку или число: ")
ex = Example()
print(ex.raschet())