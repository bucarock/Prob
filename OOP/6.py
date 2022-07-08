class Alphabet:
    bykv = ''
    for i in range(ord('А'), ord('Я') + 1):
        bykv += chr(i)
    for i in range(ord('а'), ord('я') + 1):
        bykv += chr(i)
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

import string
class EngAlphabet(Alphabet):
    __letters_num = string.ascii_letters
    def __init__(self, En, letters):
        super().__init__()

    def is_en_letter(self, x):
        if self.x in __letters_num:
            print(True)
        else:
            print(False)

    def letters_num(self):
        return (self.__letters_num)

    def example():
        print('This English Language')

if __name__ == '__main__':
    E = EngAlphabet(1, 'R')
    E.letters_num()
    Alphabet.letters_num()
    E.is_en_letter('F')
    E.is_en_letter('Щ')
    E.example()



# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

#
#     x = Alphabet()
#     x.print()
#     print(x.letters_num())



