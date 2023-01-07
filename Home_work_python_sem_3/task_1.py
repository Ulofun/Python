# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample


def num_list(num_count):
    new_list = sample(range(1, (num_count + 1) * 2), k=num_count)
    print(new_list)
    sum_digits = 0
    for i in range(0, len(new_list), 2):
        sum_digits += new_list[i]
    return sum_digits


num_count = int(input("Сумма элементов: "))

result = num_list(num_count)
print(result)
