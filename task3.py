# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19


def neWlist(lst):
    new_list = []
    for i in lst:
        new_list.append(round(i%1,4))
    return new_list


lst = list(map(float, input("Введите числа через пробел:\n").split()))
print(max(neWlist(lst)) - min(neWlist(lst)))