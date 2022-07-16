'''Задание 5
Пользователь с клавиатуры вводит количество часов.
Если полученное значение находится в диапазоне от 0 до
6 нужно вывести надпись Good Night, если в диапазоне от
6 до 13 Good Morning, если в диапазоне от 13 до 17 Good
Day, если в диапазоне от 17 до 0 Good Evening. Верхняя
граница диапазона не включается. Например, число 6
относится к 6 до 13'''

hours = 13
# 1
if hours >= 0:
    if hours <= 24:
        if hours <= 6:
            print('Good Night')
        elif hours <= 13:
            print('Good Morning')
        elif hours <= 17:
            print('Good Day')
        else:
            print('Good Evening')
    else:
        print('More than 24h')
else:
    print('Less than 0h')

# 2
if 0 <= hours <= 24:
    pass
else:
    print('Incorrect hours')
# 3
if 0 <= hours and hours <= 24:
    if hours <= 6:
        print('Good Night')
    elif hours <= 13:
        print('Good Morning')
    elif hours <= 17:
        print('Good Day')
    else:
        print('Good Evening')
else:
    print('Incorrect hours')

'''Задание 3
Пользователь вводит с клавиатуры номер месяца (от 1
до 12). В зависимости от полученного номера месяца программа выводит на 
экран надпись: Winter (если введено
значение 1,2 или 12), Spring (если введено значение от 3
до 5), Summer (если введено значение от 6 до 8), Autumn
(если введено значение от 9 до 11).
Если пользователь ввел значение не в диапазоне от 1
до 12 требуется вывести сообщение об ошибке.'''
month = 3
if month >= 3 and month <= 5:
    print('Spring')
elif month >= 6 and month <= 8:
    print('Summer')
elif month >= 9 and month <= 11:
    print('Autumn')  # Fall
elif month == 1 or month == 2 or month == 12:
    print('Winter')
else:
    print("It's imposimble")

number1 = int(input("Enter number1 : "))
command = int(input("Enter operator : "))
number2 = int(input("Enter number2 : "))
result = 0
if command == '+':
    result = number1 + number2
elif command == '-':
    result = number1 - number2
elif command == '*':
    result = number1 * number2
elif command == '**':
    result = number1 ** number2
elif number2 != 0:
    if command == '/':
        result = number1 / number2
    elif command == '//':
        result = number1 // number2
    elif command == '%':
        result = number1 % number2
if command == '+':
    result = number1 + number2
elif command == '-':
    result = number1 - number2
elif command == '*':
    result = number1 * number2
elif command == '**':
    result = number1 ** number2
elif command == '/' and number2 != 0:
    result = number1 / number2
elif command == '//' and number2 != 0:
    result = number1 // number2
elif command == '%' and number2 != 0:
    result = number1 % number2
print(result)

# warrior
# scout
# magic

main_char = 'scout'
second_char = 'warrior'

if main_char == 'warrior' and second_char == 'magic':
    print('Paladin')
elif main_char == 'scout' and (second_char == 'magic' or second_char == 'warrior'):
    print('Someone')
elif main_char == 'scout' and second_char == 'magic':  # Никогда не выполнится
    print('Druid')

a = 2
b = 3
c = 4
if a == b and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)

print('Andrey', '2', sep='')

if True:
    pass
