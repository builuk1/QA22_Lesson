# def hello_worker(name, work):  # Аргументы функции, атрибуты функции,параметры функции, передача переменной в функцию
#     print(f"Hello World!\nMy name is {name}\n I am a {work}")
#     # return f"Hello World!\nMy name is {name}\n I am a {work}"
#
# print(hello_worker('Andrii','Teacher'))#None
#
# def hello_worker_return(name, work):  # Аргументы функции, атрибуты функции,параметры функции, передача переменной в функцию
#     return f"Hello World!\nMy name is {name}\n I am a {work}"
#     print('Эта часть кода не выполниться никогда')
# print(hello_worker_return('Andrii','Teacher'))
# a = hello_worker_return('Sten','Builder')
# print(a)
#
# def pass_generator(lenth,digit,alpha):#8,True,True
#     n = '0123456789'
#     a = 'abcdef'
#     import random
#     p = ''
#     for i in range(lenth):
#         if digit and alpha:
#             p = p + random.choice(n+a)
#         elif digit:
#             p = p + random.choice(n)
#         elif alpha:
#             p = p + random.choice(a)
#     return p
#
# print(pass_generator(8,False,True))
# p_l = []
# for i in range(200):
#     p_l.append(pass_generator(8, True, True))
'''Задание 4
Напишите функцию, которая возвращает максимальное из четырёх чисел. 
Числа передаются в качестве
параметров.'''


def square(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    elif d >= a and d >= c and d >= b:
        return d


print(square(1, 1, 1, 1))

'''Задание 5
Напишите функцию, которая возвращает сумму чисел
в указанном диапазоне. Границы диапазона передаются
в качестве параметров.'''


def range_sum(number1, number2):
    sum = 0
    if number1 > number2:
        for i in range(number2, number1 + 1):
            sum = sum + i
    elif number1 < number2:
        for i in range(number1, number2 + 1):
            sum = sum + i
    elif number1 == number2:
        sum = number1
    return sum


print(range_sum(1, 36))
print(range_sum(36, 1))


def sum_num(a, b):
    sum = 0
    if a < b:

        for i in range(a, b + 1):
            sum = sum + i
        return sum
    else:
        print("Change numbers")


print(sum_num(1, 5))

'''Задание 6
Напишите функцию, которая проверяет является ли
число простым. Число передаётся в качестве параметра.
Если число простое нужно вернуть из метода true, иначе
false.'''


def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def simplev2(n):
    for i in range(2, (n // 2 + 1)):
        if n % i == 0:
            return False
    return True


print(simple(137))
print(simplev2(137))
print(simple(42))
print(simplev2(42))

'''Задание 7
Напишите функцию, которая проверяет является
ли шестизначное число «счастливым». Число передаётся в качестве параметра. 
Если число счастливое нужно
вернуть из функции true, иначе false.
«Счастливое шестизначное число» — это число у которого сумма первых 
трёх цифр равна сумме трёх вторых
цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
а 723422 – несчастливое 7+2+3 != 4+2+2.'''


def lucky(n):
    n = str(n)
    if len(n) % 2 == 0:
        n1 = n[:(len(n) // 2)]
        n2 = n[(len(n) // 2):]
    else:
        n1 = n[:(len(n) // 2) + 1]
        n2 = n[(len(n) // 2):]
    sum_n1 = 0
    sum_n2 = 0
    for number in n1:
        sum_n1 = sum_n1 + int(number)
    for number in n2:
        sum_n2 = sum_n2 + int(number)
    if sum_n1 == sum_n2:
        return True
    else:
        return False


print(lucky(12345))
print(lucky(12321))


def simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a = 137
for i in range(a):
    print(simple(i), i)
