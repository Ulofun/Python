# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# # - 1 -> нет


day = int(input())
if day > 0 and day < 8:
    if day > 5:
        print ('Выходной день')
    else:
        print ('Рабочий день')
else:
    print ('Введите корректное число дня недели')

