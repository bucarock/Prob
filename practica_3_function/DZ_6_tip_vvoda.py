# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.
def tup(b):
    print('слов', len(b))
def lis(b):
    print('букв', len(list(filter(lambda x: type(x) == str, b))), 'чисел',
          len(list(filter(lambda x: type(x) in (int, float), b))))
def stroka(b):
    print('букв', len(b))
def chislo(z):
    print(f'нечетных цифр = {z}')

def q(b):
    if type(b) == tuple:
        tup(b)
    elif type(b) == list:
        lis(b)
    elif type(b) == str:
        stroka(b)
    elif type(b) == int or type(b) == float:
        z = 0
        w = len(str(b))
        for i in range(w):
            if i % 2 != 0:
                z += 1
            else:
                continue
        chislo(z)

q((1, 2, 3))
q([1, 2, 3, 'a', 'b', 'c'])
q('abcd')
q(1234567891245)