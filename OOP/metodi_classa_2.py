class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)


class ChildClass(MyClass):
    TOTAL_OBJECTS=0
    def __init__(self):
        ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS + 1

    pass

# Создаем объекты
my_obj1 = ChildClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
# Вызываем classmethod
ChildClass.total_objects()