# '''Задание 4
# Напишите функцию, переворачивающую содержимое
# списка целых.'''
# l = [1, 2, 3, 4, 5]
# l = l[::-1]
# print(l)
# l = [1, 2, 3, 4, 5]
# print(l.reverse())
# print(l)
#
#
# # Создаёт новый список
# def my_reverse(my_list):
#     r_list = []
#     for elem in my_list:
#         r_list.insert(0, elem)
#     return r_list
#
# #Дописать
# def old_reverse(my_list):
#     for i in range(1,len(my_list)):
#         a = my_list[i]
#         b = my_list[i-1]
#         my_list[i] = b
#         my_list[i - 1] = a
#     my_list = my_list[:] #посмотрим позже
#
#
# l = [1, 2, 3, 4, 5]
# old_reverse(l)
# print(l)
# [1, 2, 3, 4, 5]
# # ?????
# [5, 4, 3, 2, 1]

# LEGB
# a = 4
# def summary():
#     #Local Локальная область видимости
#     b = 5#Создается в локальной области видимости, ВНЕ ФУНКЦИИ ЕЁ НЕТ
#     print(a+b)
#
# summary()
# #print(b)#Будет ошибка, так как программа не знает такой переменной
#
# a1 = 6
# def summary1():
#     a1 = 10
#     b1 = 10
#     print(a1 + b1)
#
# summary1()
#
# #Global Глобальная область видимости, все переменные, во всей программе ( в файле .py)
# c = 10
# d = 20
#
# def average():
#     #Local Локальная область видимости, внутри функции
#     global d#возьми из области видимости глобально и поменяй
#     print(c+d)
#     d = d + 5
#     # count = count + 1
# average()
# average()
# average()
# average()
#
# #Built-in область видимости интерпретатора
# #len()  del range() input() print()
#
# #Enclosing
# #############################
# #Global
# x = 10
# def num():
#     global x
#     #Local
#     y = 20
#     print(x+y)
#     def deep_num():
#         global x
#         nonlocal y
#         #Local???
#         z = 30
#         print(x+y+z)
#     deep_num()
#
# num()

# Рекурсия
# Бесконечная рекурсия
# def factorial():
#     print(1)
#     return factorial()
#
# print(factorial())

# Конечная рекурсия, хвостовая рекурсия
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n - 1))


print(factorial(5))


# Поиск простого числа рекурсивным методом
def simple(n):
    if n == 0:
        return 1
    else:
        return n * (simple(n - 1))


print(simple(5))
