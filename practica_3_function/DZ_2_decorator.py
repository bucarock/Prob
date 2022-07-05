# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция

a = 0
def simple_decore(fn):
    print("Start")
    global a
    fn()
    a = a+1
    print("The end!")
    print(a)

def first_test():
    print("Первый")

def second_test():
    print("Второй")

simple_decore(first_test)
simple_decore(first_test)
simple_decore(second_test)
