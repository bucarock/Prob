# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

class MYMY_1():
    volume = 0
    volumemax = 100

    @classmethod
    def tigr(cls, x):
        if cls.volume < x < cls.volumemax:
            return "В заданном диапазоне"

    def corova(self):
        return 'Му-Му'

print(MYMY_1.corova(123)) # вызываем обычный метод

class KOR():
    @staticmethod
    def UYT(sound):
        if sound == 'Му-Му':
            return 'Корова'
        else:
            return 'Другое животное'

print(KOR.UYT('Му-Му')) # Вызывает статический метод
print(MYMY_1.tigr(55))  # Вызываем класс метод