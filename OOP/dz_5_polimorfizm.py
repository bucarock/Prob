# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

class Money:
    def cash(self, z, x=None):
        if x is not None:  # 2 условия это тоже полиморфизм
            print(f'У вас все хорошо. Бабла хватает. сумма {z+x}')
        else:
            print(f'Все печально(( нужно идти на работу. сумма {z}')


bablo = Money()
bablo.cash(10000, 16000)

def second_polymorphism():
    for item in [Money]:
        print('Я бабки украл.')
        moneti = item()
        moneti.cash(1245)# moneti.cash(1245, 10000) Тогда первое условие сработает.

second_polymorphism()