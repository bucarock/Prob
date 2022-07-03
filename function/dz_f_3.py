# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе.
def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    limit = n**(1/2)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(int(input("Введите число от 0 до 1000: "))))