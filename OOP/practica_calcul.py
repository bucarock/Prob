class Calc:
    def __init__(self):# В первую очередб срабатывает ИНИТ.
        self.vvod()# вызываем функцию ввода.

    def plus(self):# функция на ПЛЮС
        return self.a + self.b

    def minus(self):# функция на МИНУС
        return self.a - self.b

    def dele(self): # функция на ДЕЛИТЬ
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def umn(self): # функция на УМНОЖИТЬ
        return self.a * self.b

    def vvod(self):# Функция на ввод чисел
        self.a = int(input("Введите первое число: "))
        self.b = int(input("Введите второе число: "))


while True:
    ex = Calc()# Запуск класса
    c = input("Введите операцию(+,*,/,-): ")
    if c == '+':
        print(ex.plus())# Вызов функции через принт, потому что реторн
    elif c == "-":
        print(ex.minus())
    elif c == '*':
        print(ex.umn())

    elif c == '0':# Выход из калькулятора через 0
        break
    else:
        print(ex.dele())