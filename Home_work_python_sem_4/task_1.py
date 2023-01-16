# Вычислить число c заданной точностью d


# Первый варинат решения

# from decimal import Decimal, getcontext
#
# number = Decimal(input("Введите натуральное число: "))
# accuracy = str(input("Введите требуемую точность в формате '0.0001': "))
# print(number.quantize(Decimal(accuracy)))


def find_prime_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num /= di
        else:
            di += 1
    return pr_fact
