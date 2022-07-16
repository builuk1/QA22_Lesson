# str        'Hello' строка                  не изменяемый, итерируемый, индексируемый тип данных
# int        5       целое число             не изменяемый, не итерируемый, не индексируемый тип данных
# float      5.2     дробное число           не изменяемый, не итерируемый, не индексируемый тип данных
# bool       True/False логический           не изменяемый, не итерируемый, не индексируемый тип данных
# list       [1,2,3.5,True,'Hello',[1,2]]    список    изменяемый, итерируемый, индексируемый тип данных
# tuple      (1,2,3.5,True,'Hello',[1,2])    кортеж не изменяемый, итерируемый, индексируемый тип данных
# dict      {'a':1, 'd': 2, True: 't' }        словарь изменяемый, итерируемый, не индексируемый тип данных
# set       {'a','b','c',1,2,3}             множество  изменяемый, итерируемый, не индексируемый содержащий только уникальные значения тип данных (ключ и значение один и тот же элемент)
# frozenset {'a','b','c',1,2,3}             множество  не изменяемый, итерируемый, не индексируемый содержащий только уникальные значения тип данных (ключ и значение один и тот же элемент)
rpg = {(0, 0, 0): 'No monster', (0, 0, 1): 'Rat'}
l = []
l = list()
t = ()
t = tuple()  # Не имееет смысла создавать пустым, так как тип данных неизменяемый.
d = {}
d = dict()
s = set()
fs = frozenset()  # Не имееет смысла создавать пустым, так как тип данных неизменяемый.
'''Задание 6
В словаре хранится набор пар: Название страны ->
Столица. Нужно реализовать функциональность по добавлению, удалению, поиску и замене.'''
countries = {'Kyiv': 'Ukraine', 'Warsaw': 'Poland', 'Berlin': 'Germany', 'Paris': 'France', 'Rome': 'Italy'}
# print(countries['Kyiv'])
# k = 'Kyiv'
# if k in countries:
#     print(countries[k])
#
# print(countries['Warsaw'])
# countries['Warsaw'] = 'France'
# print(countries['Warsaw'])
# print(countries)
# CRUD
# Create
# Read
# Update
# Delete
'''Задание 6
В словаре хранится набор пар: Название страны ->
Столица. Нужно реализовать функциональность по добавлению, удалению, поиску и замене.'''
# countries = {'Kyiv': 'Ukraine', 'Warsaw': 'Poland', 'Berlin': 'Germany', 'Paris': 'France', 'Rome': 'Italy'}
# while True:
#     command = str(input('Enter command: \n[c] - create\n[r]- read\n[u] - update\n[d] - delete\n:'))
#     if command == 'r':
#         #Read
#         for capital in countries:
#             print(f'Capital : {capital}  \tCountry : {countries[capital]}')
#     elif command == 'c':
#         #Create
#         capital = str(input('Enter capital of country : '))
#         country = str(input('Enter country : '))
#         countries[capital] = country
#     elif command == 'u':
#         #Update
#         capital = str(input('Enter capital of country : '))
#         country = str(input('Enter country : '))
#         countries[capital] = country
#     elif command == 'd':
#         #Delete
#         capital = str(input('Enter capital of country : '))
#         del countries[capital]
#
#
#


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d.items())#dict_items([('a', 1), ('b', 2), ('c', 3)])
# print(d.keys())#dict_keys(['a', 'b', 'c'])
# print(d.values())#dict_values([1, 2, 3])
# print(d.pop('a'))#Удаляет элемент по ключу. Если нет, ошибка
# print(d.popitem())#Удаляет любой элемент ( случайно, так как список неупорядоченный тип данных)
# print(d.popitem())

# Применение множеств для уникализации данных
# l = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8]
# print(l)
# l = set(l)
# print(l)
# l = list(l)
# print(l)

a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 7, 8, 9, 0}
print(a.union(b))  # Объединение множеств
print(a.difference(b))

'''
С множествами можно выполнять множество операций: находить объединение, пересечение...

len(s) - число элементов в множестве (размер множества).
x in s - принадлежит ли x множеству s.
set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
set == other - все элементы set принадлежат other, все элементы other принадлежат set.
set.issubset(other) или set <= other - все элементы set принадлежат other.
set.issuperset(other) или set >= other - аналогично.
set.union(other, ...) или set | other | ... - объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... - пересечение.
set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.copy() - копия множества.
И операции, непосредственно изменяющие множество:

set.update(other, ...); set |= other | ... - объединение.
set.intersection_update(other, ...); set &= other & ... - пересечение.
set.difference_update(other, ...); set -= other | ... - вычитание.
set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.add(elem) - добавляет элемент в множество.
set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) - удаляет элемент, если он находится в множестве.
set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
set.clear() - очистка множества.'''
