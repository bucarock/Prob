class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")


class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")


cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.radio_method()
class Test:
    def qw(self):
        print('test1')
class Test2(Test):
    def qw(self):
        print('test2')
t2 = Test2()
t2.qw()
def we(a, b):
    pass

print(we(3,2))