# Задайте список из нескольких чисел. Напишите программу, которая найдёт
#  сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

x = [2, 3, 6, 10, 12, 16, 5]

def Summ(x):
    summ = 0
    for i in range(1, len(x), 2):
        summ += x[i]
    return summ
        

print(f"{x} -> сумма элементов на нечётных позициях: {Summ(x)}")