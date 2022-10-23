# Task 1

# summ_of_digits = 0
# some_num_str = input('Введите число N: ')
# some_num_str = some_num_str.replace('.', '')
# some_array = [int(i) for i in some_num_str]
# print(some_array)

# summ = 0
# for i in some_array:
#     summ = summ + i
# print(summ)

#------------------------------------------------------------------------------------

# Task 2

# some_num = int(input('Введите число N: '))
# some_array = []

# for i in range(1, some_num + 1):
#     s = 1

#     for j in range(1, i + 1):
#         s = s * j
#     print(s)   
#     some_array.append(s)

# print(some_array)

#-------------------------------------------------------------------------------------

# Task 3

# some_num = int(input('Введите число N: '))
# some_array = []
# summ = 0
# for i in range(1, some_num + 1):
#     summ = summ + round((1 + 1/i)**i, 2)
#     some_array.append(round((1 + 1/i)**i, 2))

# print(some_array)
# print(summ)

#------------------------------------------------------------------------------------

# Task 4 - Перемешивание списка

# import random

# lst = list(range(1,21))
# print(lst)
# random.shuffle(lst)
# print(lst)

#------------------------------------------------------------------------------------

# Task 5 - Список из N элементов, заполненный числами из промежутка [-N;N]. Найти произведение элементов на позициях, указанных в файле

# from random import randint

# n = int(input('Введите число N: '))
# some_list = []
# for _ in range(n):
#     some_list.append(randint(-n, n))
# print('Сгенерированный список: ',some_list)

# with open('my_file.txt', 'r') as f:
#     data = f.read()
# lst = data.split()
# print('Считанные позиции элементов: ', lst)
# mult = 1
# for i in range(0, len(lst)):
#     mult *= some_list[int(lst[i])]
# print('Произведение элементов: ', mult)