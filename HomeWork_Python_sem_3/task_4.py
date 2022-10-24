#4. Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

N = int(input("Введите количество чисел Фибоначчи: "))
first = sec = 1
 
print('Вывод чисел Фибоначчи: ',first, sec, end=' ')
 
for i in range(2, N):
    first, sec = sec, first + sec
    print(sec, end=' ')