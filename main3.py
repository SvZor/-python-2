# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list1)))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# # решение однокурсников
# user_list = [1, 2, 3, 4, 5]
# k = 3
# res_list=[]
# res_list.extend(user_list[k:len(user_list)])
# res_list.extend(user_list[0:k])
# print(res_list)

# ## решение учителя неверное, т к 5 и 4 не переворачиваются
# list1 = [5, 4, 6, 7, -10]
# k = int(input())
# k = k % len(list1)

# list_res = []
# for i in range(k):
#     list_res.append(list1[len(list1) - 1 - i])

# print(list_res)

# for i in range(len(list1) - k):
#     list_res.append(list1[i])

# print(list_res)

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# ## решение от учителя

# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, 
#           {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
# set_1 = set()

# for i in list_1:
#     for j in i:
#         set_1.add(i[j]) # получаем множество

# print(set_1)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# list1 = [0, -1, 5, 2, 3]
# count = 0

# for i in range(1, len(list1)):
#     if list1[i] > list1[i-1]:
#         count += 1
# print(count)
