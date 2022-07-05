# Напишите пример любого класса и создайте его объект
#Допишите по 2 динамических и статических свойства в класс с предыдущего задания. Продемонстрируйте их работу
class cl_1:
    default_sound = 'мяу-мяу'
    default_color = 'black&white'
    def print(self):
        print("я изучаю классы и объекты")
    def __init__(self, sound, color):
        self.sound = sound
        self.color = color
cl_1_object = cl_1('гав-гав', 'orange')

print(cl_1_object.default_sound)
print(cl_1_object.default_color)
print(cl_1_object.sound)
print(cl_1_object.color)


class cl_2:
    def print(self):
        a = 'КУ-КУ'
        print(self)
        print(dir(cl_2))
        __str__ = 'green'
        print(__str__)
        __new__ = 123

cl_1.print('a')
cl_2.print('ку-ку')
