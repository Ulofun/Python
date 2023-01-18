# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

def words_list (num, word="абв"):
    if num >= 0:
        new_string = ""
        new_string_short = ""
        for i in range(num):
            w = sample(word, k=3)
            m = ''.join (w)
            new_string += m +" "
            if m != "абв":
                new_string_short += m +" "
        return new_string, new_string_short

number = int(input('Введите число: '))

out_string = words_list(number)
print("Первоначальная строка: ")
print(out_string[0])
print("Строка с удалёнными 'абв': ")
print(out_string[1])


