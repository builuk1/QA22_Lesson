# l1 = [1, 2, 3, 4, 5, 6, 0, 8]
# l2 = [1, 2, 3, 5, 7, 6]
# for el in l1:
#     if el in l2:
#         pass
#
# if len(l1) < len(l2):
#     length = len(l1)
# else:
#     length = len(l2)
#
# for i in range(length):
#     if l1[i] == l2[i]:
#         print(l1[i])

# Функции
# print("Hello World")
# print("Hello World")
#
#
# #Объявление функции
# def hello():
#     print("Hello World")
#
#
# #Вызов функции
# hello()
# hello()
# hello()
#
# def hello_name():
#     print("Hello World!\nMy name is Andrii")
#
# hello_name()
# hello_name()
# hello_name()

'''Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't let the noise of others' opinions
drown out your own inner voice.”
                            Steve Jobs'''


# def s_jobs():
#     print(" \"Don't let the noise of others \' opinions\n drown out your own inner voice.\"\n\t\t\t\t\tSteve Jobs")
# s_jobs()
#
# def hello_person(name):#Аргументы функции, атрибуты функции, передача переменной в функцию
#     print(f"Hello World!\nMy name is {name}")
#
# hello_person('Sten')

def hello_worker(name, work):  # Аргументы функции, атрибуты функции,параметры функции, передача переменной в функцию
    print(f"Hello World!\nMy name is {name}\n I am a {work}")


hello_worker('Teacher', 'Sten')

'''Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними.'''
# Прелюдия
a = 1
b = 36
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
# Превращение в функцию
a = 1
b = 36


def odd_numbers(a, b):
    a = int(a)
    b = int(b)
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)


odd_numbers(a, b)
odd_numbers(2, 19)

'''Задание 3
Напишите функцию, которая отображает горизонтальную или 
вертикальную линию из некоторого символа.
Функция принимает в качестве параметра: длину линии,
направление, символ.'''


def make_string(length, direction, symbol):
    for i in range(length):
        if direction == 'h':
            print(symbol, end='')
        else:
            print(symbol)
    if direction == 'h':
        print()


make_string(7, 'h', '*')
length = int(input('Enter lendth of string'))
symbol = str(input('Enter symbol'))
dir = str(input('Enter h if horizontal? and v if vertical'))


def string(length, symbol, dir):
    if dir == 'h':
        print(symbol * length)
    elif dir == 'v':
        for i in range(length):
            print(symbol)


string(length, symbol, dir)
