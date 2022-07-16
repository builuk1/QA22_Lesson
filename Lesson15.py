# str    строка      не изменяемый, итерируемый, индексируемый тип данных

# list   список      изменяемый, итерируемый, индексируемый тип данных

l = list()
l = []
l = [1, 2, 'Hello', True, False, 4.4]
#   0 , 1 , 2     ,3    , 4    , 5
print(l[2])
colors = ['Red', 'Green', 'Blue']
print(colors[1])  # Green
colors[1] = 'Yellow'
print(colors[1])  # Yellow
print(colors)
# ['Red', 'Yellow', 'Blue']
c = colors[0]
colors[0] = colors[2]
colors[2] = c
print(colors)
# ['Blue', 'Yellow', 'Red']
colors.append('Orange')  # Добавляет элемент в конец списка
print(colors.append('Orange'))  # Ничего не возвращает
print(colors)
colors.pop()  # Удаляет элемент по индексу, если индекс не указан, удаляет элемент с конца списка и возвращает его
print(colors.pop())  # Возвращает то, что "отрезал"
print(colors)
colors.insert(0, 'Purple')  # Добавляет элемент по индексу, сдвигая все остальные элементы
print(colors.insert(0, 'Purple'))  # Ничего не возвращает
print(colors)
colors.remove('Yellow')  # Удаляет элемент по содержимому, первое его вхождение
print(colors.remove('Purple'))  # Ничего не возвращает
print(colors)
print(colors.index('Red'))  # Возвращает индекс вводимого элемента ( первое вхождение)
colors.sort()  # Отсортирует список по возрастанию: чисел, алфавита 0-9, a-z
print(colors)
# Список в Python представляет из себя двусвязанный список в памяти

'''Задание 2
Пользователь с клавиатуры вводит элементы списка
целых и некоторое число. Необходимо посчитать сколько раз данное число присутствует в списке. Результат
вывести на экран. '''
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 0, 0, 4, 2, 4]
number = 4
count_of_number = 0
for n in numbers:
    if n == number:
        count_of_number = count_of_number + 1

print(count_of_number)

'''Задание 3
Пользователь с клавиатуры вводит элементы списка
целых. Необходимо посчитать сумму всех элементов
и их среднеарифметическое. Результаты вывести на
экран.'''
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 0, 0, 4, 2, 4]
summa = 0
count = len(numbers)
for number in numbers:
    summa = summa + number
average = summa / count
print(f'Sum: {summa} Average : {average}')

'''Задание 1
В списке целых, заполненном случайными числами
вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и
максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами.'''

numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 9, 0, 0, 4, 2, 4]
# 1,2,3,4
sum_negative = 0
sum_even = 0
sum_odd = 0
mult_3 = 1
for i in range(len(numbers)):  # 0,1,2,3,4,5,6,7,8,9,10
    if numbers[i] < 0:
        sum_negative = sum_negative + numbers[i]
    if numbers[i] % 2 == 0:
        sum_even = sum_even + numbers[i]
    elif numbers[i] % 2 != 0:
        sum_odd = sum_odd + numbers[i]
    if i % 3 == 0:
        mult_3 = mult_3 * numbers[i]
# 5,6
max_elem = numbers[0]
min_elem = numbers[0]
max_elem_index = 0
min_elem_index = 0
mult_min_max = 1
pos_first = numbers[0]
pos_last = numbers[0]
pos_first_index = 0
pos_last_index = 0
sum_pos = 0
for i in range(len(numbers)):
    if max_elem < numbers[i]:
        max_elem = numbers[i]
        max_elem_index = i
    if min_elem > numbers[i]:
        min_elem = numbers[i]
        min_elem_index = i

if max_elem_index < min_elem_index:
    c = min_elem_index
    min_elem_index = max_elem_index
    max_elem_index = c

for elem in numbers[min_elem_index:max_elem_index]:
    mult_min_max = mult_min_max + elem

for i in range(len(numbers)):
    if numbers[i] > 0:
        pos_first = numbers[i]
        pos_first_index = i
for i in range(1, len(numbers)):
    if numbers[-i] > 0:
        pos_last = numbers[i]
        pos_last_index = -i

for elem in numbers[pos_first_index:pos_last_index]:
    sum_pos = sum_pos + elem

numbers = [-5, -3, -1, -6, 3, 4, -10, 6, 2, 10]
summUnderZero = 0
summEven = 0
summNotEven = 0
multiplyIndex = 1
multiplyBetweenMinMax = 1
summFirstLast = 0
minElementIndex = 0
maxElementIndex = 0
minNumber = numbers[0]
maxNumber = numbers[0]
firstElementIndex = -1
lastElementIndex = -1
counter = 0
for number in numbers:
    if number < 0:
        summUnderZero += number
    if number % 2 == 0:
        summEven += number
    else:
        summNotEven += number
    if counter % 3 == 0:
        multiplyIndex *= number
    if number < minNumber:
        minNumber = number
        minElementIndex = counter
    if number > maxNumber:
        maxNumber = number
        maxElementIndex = counter
    if number > 0 and firstElementIndex == -1:
        firstElementIndex = counter
    if number > 0 and lastElementIndex < counter:
        lastElementIndex = counter
    counter += 1
# print(f"{minElementIndex} - {minNumber} / {maxElementIndex} - {maxNumber}")
# print(f"{firstElementIndex} - {lastElementIndex}")
for number in range(minElementIndex, maxElementIndex + 1):
    multiplyBetweenMinMax *= numbers[number]
for number in range(firstElementIndex, lastElementIndex + 1):
    summFirstLast += numbers[number]
print(f"=== 1 === \n {summUnderZero}")
print(f"=== 2 === \n {summEven}")
print(f"=== 3 === \n {summNotEven}")
print(f"=== 4 === \n {multiplyIndex}")
print(f"=== 5 === \n {multiplyBetweenMinMax}")
print(f"=== 6 === \n {summFirstLast}")
