# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000


def dec_number(number):
    binary = 0
    decade = 1
    while number > 0:
        binary = binary + number % 2 * decade
        number //= 2
        decade *= 10
    return binary


num = int(input('Введите натуральное число: '))
bin_number = dec_number(num)
print(f'Число {num} в двоичной системе выглядит как {bin_number}')


# def conv_bin(num: int):
#     list_nums = []
#     while num > 0:
#         list_nums.insert(0, num % 2) # добавляет новый элемент списка на индекс[0] на каждой итерации
#         num //= 2
#     print(*list_nums, sep="")
#
# conv_bin(int(input('Введите натуральное число: ')))