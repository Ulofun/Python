#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

n = int(input("Введите десятичного число: "))
x = ""
while n != 0:
    x = str(n % 2) + x
    n //= 2
print('Результат преобразования: ',x)
