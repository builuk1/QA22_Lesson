# str        'Hello' строка                  не изменяемый, итерируемый, индексируемый тип данных
# int        5       целое число             не изменяемый, не итерируемый, не индексируемый тип данных
# float      5.2     дробное число           не изменяемый, не итерируемый, не индексируемый тип данных
# bool       True/False логический           не изменяемый, не итерируемый, не индексируемый тип данных
# list       [1,2,3.5,True,'Hello',[1,2]]    список    изменяемый, итерируемый, индексируемый тип данных
# tuple      (1,2,3.5,True,'Hello',[1,2])    кортеж не изменяемый, итерируемый, индексируемый тип данных

# for letter in 'Hello world!':
#     print(letter)

# l = [1,2,3]
# a = l
# l.pop()
# a.append(4)
# print(l)
# print(a)
#
# l = [1,2,3]
# a = l[:]
# l.pop()
# print(l)
# print(a)

l = [1, 2, 3.5, True, 'Hello', [1, 2]]
t = (1, 2, 3.5, True, 'Hello', [1, 2])
print(l.__sizeof__(), t.__sizeof__())
l = list()
l = []
t = tuple()
a = 5
b = 2
(a, b) = (b, a)
print(a, b)
'''Есть список целых, заполненный случайными числами.
На основании данных этого массива нужно:
■ Создать список целых, содержащий только четные
числа из первого списка;
■ Создать список целых, содержащий только нечетные
числа из первого списка;
■ Создать список целых, содержащий только отрицательные числа из первого списка;
■ Создать список целых, содержащий только положительные числа из первого списка.'''
l = [1, -2, 3, 4, -5, 6, 7, 8, -9, 11, 13, 12, 137, 18]
odd = []
even = []
neg = []
pos = []
for elem in l:
    if elem % 2 == 0:
        even.append(elem)
    if elem % 2 != 0:
        odd.append(elem)
    if elem > 0:
        pos.append(elem)
    if elem < 0:
        neg.append(elem)
print(odd, even, neg, pos)

l = [1, -2, 3, 4, -5, 6, 7, 8, -9, 11, 13, 12, 137, 18]
w_odd = []
w_even = []
w_neg = []
w_pos = []

while l:
    elem = l.pop(0)
    if elem % 2 == 0:
        w_even.append(elem)
    if elem % 2 != 0:
        w_odd.append(elem)
    if elem > 0:
        w_pos.append(elem)
    if elem < 0:
        w_neg.append(elem)
print(w_odd, w_even, w_neg, w_pos)

t = tuple(l[:])
print(t)

'''Задание 1
Пользователь вводит с клавиатуры название фрукта.
Необходимо вывести на экран количество раз, сколько
фрукт встречается в кортеже в качестве элемента.
Задание 2
Добавьте к заданию 1 подсчет количества раз, когда
название фрукта является частью элемента. Например:
banana, apple, bananamango, mango, strawberry-banana.
В примере выше banana встречается три раза.'''
# 1
t = ('Banana', 'Apple', 'Pineapple', 'Orange', 'Cranberry', 'Strawberry', 'Blackberry', 'Berry')
fruit = 'Berry'
fruit_count = 0
for elem in t:
    if fruit == elem:
        fruit_count = fruit_count + 1

print(fruit_count, t.count(fruit))

# 2
t = ('Banana', 'Apple', 'Pineapple', 'Orange', 'Cranberry', 'Strawberry', 'Blackberry', 'Berry')
fruit = 'Berry'
fruit_count = 0
for elem in t:
    if fruit.lower() in elem.lower():
        fruit_count = fruit_count + 1
print(fruit_count)

'''Задание 4
Есть кортеж с целыми числами. Нужно вывести статистику по 
количеству цифр в элементах кортежа. 
Например:
■ Одна цифра — 3 элемента;
■ Две цифры — 4 элемента;
■ Три цифры — 5 элементов.'''
t = (111, -22, 31, 45, -52, 116, 7, 118, -229, 311, 13, 122, 137, 18)
n1 = 0
n2 = 0
n3 = 0
# 1
for elem in t:
    e = str(elem)
    if e[0] == '-':
        e = e[1:]
    l_e = len(e)
    if l_e == 1:
        n1 = n1 + 1
    elif l_e == 2:
        n2 = n2 + 1
    elif l_e == 3:
        n3 = n3 + 1
n1 = 0
n2 = 0
n3 = 0
# 2
for elem in t:
    e = elem
    if e < 0:
        # e = e * (-1)
        e = -e
    s1 = e // 100
    s2 = (e // 10) % 10
    s3 = e % 10

    if s1 == 0:
        n2 = n2 + 1
    elif s1 == 0 and s2 == 0:
        n1 = n1 + 1
    elif s1 == 0 and s2 == 0 and s3 == 0:
        continue
    else:
        n3 = n3 + 1
