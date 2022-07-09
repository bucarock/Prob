import string


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self.__letters_num = len(self.letters)

    def is_en_letter(self, symbol):
        if symbol in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return self.__letters_num

    def example(self):
        return 'My name is Nikita'


if __name__ == '__main__':
    x = EngAlphabet()
    x.print()
    print(x.letters_num())
    print(x.is_en_letter('F'))
    print(x.is_en_letter('Щ'))
    print(x.example())