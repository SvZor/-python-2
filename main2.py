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

# ##Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# # Словари
# # 💡 Словари — неупорядоченные коллекции произвольных объектов с
# # доступом по ключу.
# # В списках в качестве ключа используется индекс элемента. В словаре для
# # определения элемента используется значение ключа (строка, число).
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# # Множества
# # 💡 Множества содержат в себе уникальные элементы, не обязательно
# # упорядоченные.
# # Одно множество может содержать значения любых типов. Если у Вас есть два
# # множества, Вы можете совершать над ними любые стандартные операции,
# # например, объединение, пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()
# # Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
# 9
# # Неизменяемое или замороженное множество(frozenset) — множество, с которым
# # не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# # List Comprehension
# # У каждого языка программирования есть свои особенности и преимущества. Одна
# # из культовых фишек Python — list comprehension (редко переводится на русский, но
# # можно использовать определение «генератора списка»). Comprehension легко
# # читать, и их используют как начинающие, так и опытные разработчики.
# # List comprehension — это упрощенный подход к созданию списка, который
# # задействует цикл for, а также инструкции if-else для определения того, что в итоге
# # окажется в финальном списке.
# # 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# #2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]
# # Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# # Решение:
# # 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# #Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# 11
# #2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# #Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]
# # Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# # значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]
