# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
import random


def mult_lst(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    if len(new_lst) % 2 !=0:
        new_lst[-1] = lst[len(lst) // 2]
    return new_lst


def num_list(num_count):
    new_list = random.sample(range(1, (num_count + 1) * 2), k=num_count)
    return new_list


num = int(input("Введите размер списка: "))
n_list = num_list(num)
print(n_list)
m_list = mult_lst(n_list)
print(m_list)

# Второй способ решения:

# def mult_lst(lst):
#     l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
#     new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
#     print(new_lst)
#
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)