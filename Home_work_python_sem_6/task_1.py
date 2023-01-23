# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample


def values_previous_element(any_list):
    my_list = sample(range(any_list * 3), any_list)
    print(my_list)
    return [my_list[any_list] for any_list in range(1, len(my_list)) if my_list[any_list] > my_list[any_list - 1]]


print(values_previous_element(int(input('Введите число: '))))
