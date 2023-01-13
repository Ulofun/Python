
#Вычислить число c заданной точностью d




from decimal import Decimal, getcontext
number = Decimal(input("Введите натуральное число: "))
accuracy = str(input("Введите требуемую точность в формате '0.0001': "))
print(number.quantize(Decimal(accuracy)))
