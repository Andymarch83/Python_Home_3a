'''
Задача 18: Требуется найти в массиве A[1..N] самый
близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество
элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''

import random

lim_arr = int(input('Введите предел массива N: '))
my_arr = [random.randint(0, 10) for _ in range(1, lim_arr + 1)]
print(my_arr)
my_arr = list(set(my_arr))
# print(my_arr)
number = int(input('Введите число : '))
min_list = [i for i in my_arr if i <= number]
# for i in my_arr:
#    if i <= number:
#        min_list.append(i)
# print(min_list)
max_list = [i for i in my_arr if i >= number]
# print(max_list)
if max_list[0] == min_list[-1] or (max_list[0] - number) > (number - min_list[-1]):
    print(f'Ближайшее число: {min_list[-1]}')
elif (max_list[0] - number) == (number - min_list[-1]):
    print(f'Ближайшие числа: {min_list[-1]} и {max_list[0]}')
else:
    print(f'Ближайшее число: {max_list[0]}')
