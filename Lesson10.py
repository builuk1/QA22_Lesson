# '''Задание 3
# Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран
# будет такой: *******.'''
# '''Задание 4
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране горизонтальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и &, тогда вывод на
# экран будет такой: &&&&&.'''
# length = 7
# line = length * '*'
# print(line)
#
# length = 7
# symbol = '*'
# second_line = ''
# while length > 0:
#     second_line = second_line + symbol
#     length = length - 1
# print(second_line)

# Guess my number
# import random
# guess_number = 0
# secret_number = random.randint(1, 20)#10
# while secret_number != guess_number:
#     guess_number = int(input("Enter secret number in range [1-20] : "))
#     if secret_number > guess_number:
#         print('Your number less than secret')
#     elif secret_number < guess_number:
#         print('Your number greater than secret')
#     if secret_number == guess_number:
#         print('You win!')
#         print(secret_number)
#         secret_number = random.randint(1, 20)

import random

game = True
while game:  # while True , но тогде не получится выйти исходя из того, что мы уже умеем
    guess_number = 0
    secret_number = random.randint(1, 20)  # 10
    count_of_try = 0
    while secret_number != guess_number:
        guess_number = int(input("Enter secret number in range [1-20] : "))
        if secret_number > guess_number:
            print('Your number less than secret')
        elif secret_number < guess_number:
            print('Your number greater than secret')
        count_of_try = count_of_try + 1
    print(f'You win! Your count of tryies {count_of_try} Secret number is {secret_number}')
    game = str(input("Press [any key] + [enter] to continue \n or press [enter] to exit :"))
# legacy

'''Задание 3
Написать программу подсчета стоимости разговора
для разных мобильных операторов. Пользователь вводит
стоимость разговора и выбирает с какого на 
какой оператор он звонит. Вывести стоимость на экран'''
operator1 = str(input('Choose operator1 : [m]ts, [l]ifecell, [k]ievstar'))
operator2 = str(input('Choose operator2 : [m]ts, [l]ifecell, [k]ievstar'))
price = int(input('Your money : '))
if operator1 == operator2:
    print('Звонки в сети бесплатны')
else:
    print(f'Your price : {price}')
