# Класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) lang - язык и
# 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# Класс EngAlphabet
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв
# алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
import string
class Alphabet:
    letters = ''
    for i in range(ord('А'), ord('Я') + 1):
        letters += chr(i)
    for i in range(ord('а'), ord('я') + 1):
        letters += chr(i)
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print(letters_num)
    def letters_num(self, letters):
        return len(letters)

class EngAlphabet(Alphabet):
    __letters_num = string.ascii_letters
    def __init__(self, En, letters):
        super().__init__()

# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится
# ли эта буква к английскому алфавиту.
    def is_en_letters(self, a):
        if a in __letters_num:
            print(True)
        else:
            print(False)

# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства
# __letters_num.
    def letters_num(self):
        print(_Alphabet__letters_num)

# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке

if __name__ == '__main__':

# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке
