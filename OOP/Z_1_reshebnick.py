# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
# (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае
# наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
class soda:
    def show_my_drink(self, abc = None):
        if abc is not None:
            print(f'Газировка и {abc}')
        else:
            print('Обычная газировка')
s = soda()
s.show_my_drink('клубника')
s.show_my_drink()

class soda2:
    def __init__(self, ing):
        if isinstance(ing, str):
            self.ing = ing
        else:
            self.ing = None
    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print('Обычная газировка')
S1 = soda2('Малина')
S1.show_my_drink()
S2 = soda2('')
S2.show_my_drink()