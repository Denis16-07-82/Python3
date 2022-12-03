# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def mult_lst(lst):
    new_lst = list()
    if len(lst) % 2 != 0:
        l = len(lst)//2 + 1  
    else: 
        l = len(lst)//2

    for i in range (l):
        new_lst.append(lst[i]*lst[len(lst)-i-1])
    print(new_lst)


lst = [2, 3, 4, 5, 6]
mult_lst(lst)

