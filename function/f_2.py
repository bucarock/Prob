def func_1():
    print('hello')

def func_2(d,c, a = 5,b = 4):
    return a+b+c+d

def func_3(*args,**kwargs):
    print(args)
    print(kwargs)


func_3(1,2,3,5,5,8,9,a=2,b=5,g=8,t=6)
# print(func_2(3,5))



# c = int(input())
# print(func_2(c,int(input())))
