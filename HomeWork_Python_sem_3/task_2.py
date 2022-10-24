#2. Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

x = int(input('Введите размер списка: '))
list = []

for i in range(x):
    list.append(round(uniform(1, 9), 2)) 
print('Заданный список: ',list)

min = 1
max = 0   
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
dif = max - min 
print('Максимальная дробная часть: ', round(max, 2))
print('Минимальная дробная часть: ', round(min, 2))
print('Разница между максимальным и минимальным значением: ', round(dif,2))

