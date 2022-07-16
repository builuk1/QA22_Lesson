# Строки
# str
s = 'Hello World!'
# #    0123456789
# print(s)
# for elem in s:  # 'Hello World!'
#     print(elem)
# a = s[0]
# print(s[0], s[1], s[2], s[3])
#
# n = 'Andrii Builuk'
# print(n[2], n[3], n[4], n[1], n[12])
# # d r i n k
# print(n[0], n[1], n[2])
# # A n d
# print(n[3], n[8], n[10], n[10])
# #r u l l
# print(n[7], n[8], n[10], n[7])
# #B u l B
# print(n[3], n[8], n[10], n[10])
# #r u l l
s = 'Hello World!'
#    0123456789
# -     987654321
print(s[-1])  # справа налево, начиная с -1   !
print(s[6:11])  # World
print(s[:5])  # Hello
print(s[6:])  # World!
len(s)  # length длинну возвращает длинну любого итерируемого объекта
# str string Индексируемый, не изменяемый тип данных
# s = 'Andrii'
'''Задание 1
Пользователь вводит с клавиатуры строку. Произведите поворот строк 
и полученный результат выведите
на экран.'''
# 1
s = 'Hello World!'
s1 = ''
for letter in s:
    s1 = letter + s1  # lleH
print(s, s1)
# 2
s = 'Hello World!'
s1 = ''
for i in range(1, len(s) + 1):  # 1,2,3,4,5,6,7,8,9,10,11,12
    s1 = s1 + s[-i]
print(s, s1)
# 3
s = 'Hello World!'
s1 = s[::-1]
print(s, s1)
print(s[-5])
'''Задание 2
Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
количества на экран.'''
# 1
letters = 0
digits = 0
word = 'QwertY123456'
for element in word:
    if element == '0' or element == '1' or element == '2' or element == '3' or element == '4' or element == '5' or element == '6' or element == '7' or element == '8' or element == '9':
        digits = digits + 1
    else:
        letters = letters + 1
print(letters, digits)
# 2
letters = 0
digits = 0
word = 'QwertY123456'
number = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for element in word:
    if element in number:
        digits = digits + 1
    elif element in alpha:
        letters = letters + 1
    else:
        print('Something else')
print(letters, digits)
# 2.1
letters = 0
digits = 0
word = 'QwertY123456'
number = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for element in word:  # 'QwertY123456'
    for n in number:  # '0123456789'
        if n == element:
            digits = digits + 1
    for l in alpha:  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if l == element:
            letters = letters + 1
print(letters, digits)
# 3
letters = 0
digits = 0
word = 'QwertY123456'
for element in word:
    if element.isdigit():
        digits = digits + 1
    elif element.isalpha():
        letters = letters + 1
print(letters, digits)
