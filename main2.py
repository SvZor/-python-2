list_1 = []
print(list_1)
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(*list_1) #печать списка без квадратных скобок
# # добавлять значения в список - append -  в конец списка
# list_1.append(10)
# print(list_1)
# for i in range(5):            #цикл добавляет цифры от 0 до 4
#     list_1.append(i)
#     print(list_1)   #печатает каждое добавление

# ## удаление последнего элемента списка 
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) #0
# print(list_1) # [12, 7 -1, 21]
# print(list_1.pop()) #21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) #-1
# print(list_1) # [12, 7]

# ## удаление конкретного элемета из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) #12
# print(list_1) # [7, -1, 21, 0]

# ## Добавление элемента в нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 17))
# print(list_1) # [12, 7, 17, -1, 21, 0]

# ## работа со срезами
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# ## Кортеж — это неизменяемый список.
# ## Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
# ## каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
# ## меньше места в памяти и работают быстрее, по сравнению со списками

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
#     t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)


