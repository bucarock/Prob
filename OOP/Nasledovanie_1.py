class Phone:

    # Инициализатор
    def __init__(self):
        self.is_on = False

    # Включаем телефон
    def turn_on(self):
        self.is_on = True

    # Если телефон включен, делаем звонок
    def call(self):
        if self.is_on:
            print('Making call...')

# Унаследованный класс
class MobilePhone(Phone):

    # Добавляем новое свойство battery
    def __init__(self):
        super().__init__()
        self.battery = 0

# Заряжаем телефон на величину переданного значения
    def charge(self, num):
        self.battery = num
        print(f'Charging battery up to ... {self.battery}%')

my_mobile_phone = MobilePhone()
print(dir(my_mobile_phone))