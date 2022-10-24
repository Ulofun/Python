# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = 5
lst = []
result = 1

for i in range(n):
    lst.append(randint(n * -1, n))
print(lst)

with open('/home/daria/GB/python/homeworks/hw_2/file.txt', 'r') as pos:
    for i in pos:
        result *= lst[int(i) - 1]
    print('произведение чисел на позициях из файла:', result)