# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))


def boolFank(n): # Функция типа void ,ничего не возвращает.
    s = ""
    while n != 0:
        s = str(n%2) + s
        n = n//2
    print (s)

boolFank(n)