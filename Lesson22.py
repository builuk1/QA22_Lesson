'''
Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат
из некоторого символа. Функция принимает в качестве параметров:
длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
'''


# switcher = str(input("Enter [T]rue / [F]alse : "))
# symbol = '*'
# length = 5
# space = ' '
# square = ''
def displaying_an_empty_or_filled_square(length, symbol, switcher=False):
    space = ' '
    square = ''
    symb_leng = len(symbol)
    if switcher:
        for i in range(length):
            square = square + length * symbol + '\n'
    else:
        for i in range(length):
            if i == 0 or i == (length - 1):
                square = square + (length * symbol) + '\n'
            else:
                square = square + symbol + ((length - 2) * symb_leng * space) + symbol + '\n'
    print(square)


displaying_an_empty_or_filled_square(3, '||')
displaying_an_empty_or_filled_square(5, '**', True)
displaying_an_empty_or_filled_square(7, '* *')
displaying_an_empty_or_filled_square(8, '+', 'True')

# # НЕ ПРАВИЛЬНО
# choice = 'K'
# if choice == 'R' or 'S':  # False or True
#     print('WORK ALWAYS')
#
# choice = 'R'
# if choice == 'R' or 'S':  # True or True
#     print('WORK ALWAYS')
# # ПРАВИЛЬНО
# if choice == 'R' or choice == 'S':  # False or True
#     print('WORK SOMETIMES')
#
# choice = 'R'
# if choice == 'R' or choice == 'S':  # True or True
#     print('WORK SOMETIMES')

# # Files
# f = open('example.txt', 'wt')#w - write t - text при записи, если файл есть, его перезапишет, если файла нет, его создаст
# f.close()
#
# f = open('example.txt', 'wt')
# f.write('Hello world!\n')
# f.write('Hello world!')
# f.close()
#
# #Так делать не советую
# f = open('example.txt')#rt - по умолчанию
# print(f.read())#Считывает весь файл целиком, опасно, ОЗУ может не вместить
# f.close()
#
# f = open('example.txt','rt')# r - read t - text
# print(f.read())
# f.close()
#
# f = open('example.txt','rt')# r - read t - text
# print(f.readline())#Считывает одну строку, использует файл, как итерируемы объект, безопасно
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
#
# f = open('example.txt','rt')# r - read t - text
# print(f.readlines())#Считывает все строки, как список, использует файл, как итерируемы объект, безопасно
# f.close()

# f = open('number.txt', 'wt')
# for i in range(100, 200):
#     f.write(f'{i}\n')
#
# f.close()
#
# f = open('number.txt', 'rt')
# print(f.read())
# f.close()
#
# #Правильно
f = open('number.txt', 'rt')
s = f.readline()
while s:
    print(s)
    s = f.readline()
f.close()

# #НЕ Правильно
# f = open('number.txt', 'rt')
# while f.readline():
#     print(f.readline())
# f.close()

# Precondition
f = open('number.txt', 'wt')
for i in range(1, 36 + 1):
    f.write(f'{i}\n')

f.close()
'''Написать программу которая суммирует все числа в файле'''
f = open('number.txt', 'rt')
sum = 0
s = f.readline()
while s:
    s = float(s[:-1])
    sum = sum + s
    s = f.readline()
f.close()
print(sum)

word = 'Star'
f = open('sw.txt', 'rt')
s = f.readline()
while s:
    if word.lower() in s.lower():  # Без lower - регистрозависимое
        print(s)
    s = f.readline()
f.close()
