age = 13
gender = 'male'  # 'female'
# if age < 18:
#     print('You are a child')
# else:
#     print('You are an adult')

if gender == 'male':
    if age < 18:
        print('You are a boy')
    else:
        print('You are a man')
elif gender == 'female':
    if age < 18:
        print('You are a girl')
    else:
        print('You are a woman')
else:
    if age < 18:
        print('You are a child')
    else:
        print('You are an adult')

x = 5
y = 5
if x > 0:
    if y > 0:
        print('I')
    elif y < 0:
        print('IV')
    else:
        print('Axis X+')
elif x < 0:
    if y > 0:
        print('II')
    elif y < 0:
        print('III')
    else:
        print('Axis X-')
else:
    if y > 0:
        print('Axis Y+')
    elif y < 0:
        print('Axis Y-')
    else:
        print('Zero')

'''Задание 1
Пользователь вводит с клавиатуры число. Необходимо проверить его на 
четность и нечетность. Если число
четное требуется вывести на экран число и надпись Even
number. Если число нечетное выведите на экран число и
надпись Odd number. '''

number = 3
if number == 0:
    print('Zero')
elif number % 2 == 0:
    print('Even')
elif number % 2 != 0:
    print('Odd')

'''Задание 2
Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. 
Если число кратно
требуется вывести на экран число и надпись Number is
multiple 7. Если число не кратно выведите на экран число
и надпись Number is not multiple 7. '''

a = 'Hello'
print(a)
