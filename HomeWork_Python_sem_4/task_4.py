# ЗАДАЧА №4: Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 
# k = 6
#    ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h = 0
#    a, b, c, d, e, h - рандом

from random import randint

k = int(input('Введите степень: '))
for i in range(k,0,-1):                 # пробегаемся по коэффициенту от заданного до 0
    ratios = randint(1,101)             # случайным образом задаются коэффициенты a,b,c,d,e,h
    if i == 1:
        ratios = ''
    else:
        if i != 1:
            res = f'{ratios}*x^{i}+'    # присваиваем переменной res значение коэффициента в степени 
        else:
            res = f'{ratios}*x+'
    print(res, end=' ')                 
print(f'{randint(1,101)}=0')                 

