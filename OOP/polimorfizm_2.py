# создаем класс Car
class Car:
    def start(self, a, b=None):
        if b is not None:  # 2 условия это тоже полиморфизм
            print(a + b)
        else:
            print(a)


car_a = Car()
car_a.start(10, 15)

