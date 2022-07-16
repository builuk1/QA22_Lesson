# def triple(word1, word2, word3):
#     return f'{word1} {word2} {word3}'
#
#
# print(triple('big', 'red', 'dog'))
#
#
# def sum_some(a, b, c, d):
#     return a + b + c + d
#
#
# print(sum_some(1, 2, 3, 4))
#
#
# def sum_list(l):
#     sum = 0
#     for number in l:
#         sum = sum + number
#
#     return sum
#
#
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum_list(l))
# print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#
#
# def make_string(length, symbol='*',
#                 dir='horizontal'):  # symbol='*' аргумент по умолчанию. Если не присвоить ему значение, при запуске функции, он берёт то, что указано при её создании.
#     s = ''
#     if dir == 'horizontal':
#         s = symbol * length
#     elif dir == 'vertical':
#         for i in range(length):
#             s = s + symbol + '\n'
#
#     return s
#
#
# print(make_string(7))
#
#
# def sum_all(*args):  # * создаёт возможность, добавить любое количество аргументов
#     sum = 0
#     for number in args:
#         sum = sum + number
#
#     return sum
#
#
# print(sum_all(1, 2, 3, 4, 5, 7, 8, 9, 0, 12, 3, 4, 57, 18))
#
#
# def sum_all_string(*args):  # * создаёт возможность, добавить любое количество неупорядоченых аргументов
#     sum = ''
#     for number in args:
#         sum = sum + str(number)
#
#     return sum
#
#
# def make_string(*settings):
#     length, symbol, dir = settings  # [length,symbol,dir]
#     # symbol='*' аргумент по умолчанию. Если не присвоить ему значение, при запуске функции, он берёт то, что указано при её создании.
#     s = ''
#     if dir == 'horizontal':
#         s = symbol * length
#     elif dir == 'vertical':
#         for i in range(length):
#             s = s + symbol + '\n'
#
#     return s
#
#
# print(sum_all_string(1, 2, 3, 4, 5, 7, 8, 9, 'hello', 0, 12, 3, 4, 57, 18))
#
#
# def user_list(**users):  # ** kwargs keyword arguments аргументы с ключами, возвращает словарь dict
#     return users
#
#
# print(user_list(andrii=123456, sten='qwerty', ben='tyuevv'))
#
#
# def example(a, b, c=3, *d, **e):  # example of parameter order
#     pass
#
#
# print(example('Hello', 2))  # Не будет ошибкой, так как аргумент по умолчанию передаст (c) 3, *d = [], **e = {}
# print(example('Hello', 2, 3, 3, 3, 3, 3, 4, 5,
#               non=4))  # Не будет ошибкой, так как аргумент по умолчанию передаст (c) 3, *d = [], **e = {}
#
#
def user_money(*money_list, **user_list):
    # money_list кортеж
    # user_list словарь
    user_name_list = list(user_list.keys())
    for i in range(len(money_list)):
        user_list[user_name_list[i]] = user_list[user_name_list[i]] + money_list[i]

    return user_list


print(user_money(1000, 2000, 3000, andrii=2000, sten=3000, glen=4000, den=3000))

'''Задание 1
Напишите функцию, вычисляющую сумму элементов
списка целых. Список передаётся в качестве параметра. '''
# def sum_all(*args):  # * создаёт возможность, добавить любое количество аргументов
#     sum = 0
#     for number in args:
#         sum = sum + number
#
#     return sum
#
#
# print(sum_all(1, 2, 3, 4, 5, 7, 8, 9, 0, 12, 3, 4, 57, 18))
'''Задание 2
Напишите функцию для нахождения максимума в
списке целых. Список передаётся в качестве параметра. 
'''


def maximum(*numbers):  # [[1,2,3,7,5,67,7],]
    # if len(numbers) == 1:
    #     numbers = numbers[0]
    if len(numbers) == 1 and type(numbers[0]) == list:
        numbers = numbers[0]
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(maximum(1, 2, 3, 4, 44, 5, 6, 7, 8))
print(maximum([1, 2, 3, 4, 44, 5, 6, 7, 8]))
print(maximum(2))
