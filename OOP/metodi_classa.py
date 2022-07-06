# class Myclass():
#     @staticmethod     # Статические методы. через собаку.
#     def staticmethod():
#         print('static method called')
#
#
# class children_My_class(Myclass):
#     pass
#
#
# my_obj = Myclass()
# my_obj.staticmethod()
# my_obj_1 = children_My_class()
# my_obj_1.staticmethod()

class Person():
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

print(Person.is_adult(15))