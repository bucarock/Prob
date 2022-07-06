# Класс Human
# 1. Создайте класс Human
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два
# параметра: name и age. Для этих параметров задайте значения по
# умолчанию, используя свойства default_name и default_age. В методе
# __init__() определите четыре свойства: Публичные - name и age. Приватные
# - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name,
# age, house и money.
# 5. Реализуйте справочный статический метод default_info(), который будет
# выводить статические поля default_name и default_age.
# 6. Реализуйте метод earn_money(), увеличивающий значение свойства money.
class Human:
    default_name = "No name" # Статическое поле
    default_age = 0  # Статическое поле

    def __init__(self, name=default_name, age=default_age):
        self.name = name  # Динамическое поле
        self.age = age   # Динамическое поле
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f"Вы заработали {amount}. У Вас {self.__money} денег")


if __name__ == '__main__':# Означает что только здесь будет работать это проверка
    Human.default_info()
    Alex = Human('Alex', 25)
    Alex.info()
    Alex.earn_money(10000)
    Alex.earn_money(5000)
    Alex.info()

#    from Human import Human     Позволит импортировать класс Human в другой файл.