x = -5
y = -5
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
        print('Axis X-')  ##4
else:
    if y > 0:
        print('Axis Y+')
    elif y < 0:
        print('Axis Y-')
    else:
        print('Zero')

# and or not

print(True and True)
print(True and False)
print(False and False)
print()
print(True or True)
print(True or False)
print(False or False)
x = 5
y = 5

if x > 0 and y > 0:
    print('I')
elif x > 0 and y < 0:
    print('IV')
elif x > 0 and y == 0:
    print('Axis X+')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x < 0 and y == 0:
    print('Axis X-')
elif x == 0 and y > 0:
    print('Axis Y+')
elif x == 0 and y < 0:
    print('Axis Y-')
elif x == 0 and y == 0:
    print('Zero')

'''Задание 1
Пользователь вводит с клавиатуры время в секундах, прошедшее с начала дня. 
В зависимости от выбора
пользователя посчитать, сколько часов, минут и секунд
осталось до полуночи.'''
seconds_in_day = 86400
command = str(input("Enter number : [h],[m],[s] :"))
seconds = int(input("Enter count of seconds : "))
if command == 's':
    print(f'For midnight left {seconds_in_day - seconds} seconds')
elif command == 'm':
    print(f'For midnight left {seconds_in_day // 60 - seconds // 60} minutes')
elif command == 'h':
    print(f'For midnight left {(seconds_in_day // 60) // 60 - (seconds // 60) // 60} hours')

print('End')

'''Задание 2
Пользователь вводит с клавиатуры диаметр окружности. 
В зависимости от выбора пользователя посчитать
площадь или периметр окружности.'''

diam = float(input("enter diameter :"))
command = str(input("Enter change square or perimeter : [p], [d] :"))
pi = 3.14
if command == 'p':
    print(f'Perimetr is {diam * pi}')
elif command == 'd':
    print(f'Square is {((diam / 2) ** 2) * pi}')
    print(f'Square is {((diam / 2) * (diam / 2)) * pi}')

'''Задание 3
Пользователь вводит с клавиатуры стоимость одной
игровой приставки, их количество и процент скидки.
В зависимости от выбора пользователя посчитать общую
сумму заказа или стоимость одной приставки с учетом
скидки.'''
cost = float(input("Enter your cost : "))
quantity = int(input("Enter your quantity : "))
interest = int(input("Enter your interest : "))
if quantity == 1:
    print(f"Final cost is {((cost / 100) * (100 - interest))}")
else:
    print(f"Final cost is {(cost * quantity) / 100 * (100 - interest)}")

###
command = str(input("Enter your purchase option : [all],[one] :"))
cost = float(input("Enter your cost : "))
interest = int(input("Enter your interest : "))
if command == "one":
    print(f"Final cost is {((cost / 100) * (100 - interest))}")
elif command == "all":
    quantity = int(input("Enter your quantity : "))
    print(f"Final cost is {(cost * quantity) / 100 * (100 - interest)}")
'''Задание 4
Пользователь вводит с клавиатуры размер файла
в гигабайтах и скорость интернет-соединения в битах в секунду. 
В зависимости от выбора пользователя посчитать,
за сколько часов или минут, или секунд скачается файл.'''
size = float(input('Enter size Gb :'))
speed = float(input('Enter speed b/s :'))
command = str(input("Enter change hours minutes or seconds:[h], [m], [s] :"))

if command == 'h':
    print(f'Count is {1024 * 8 * size * speed}')
elif command == 'm':
    print(f'Square is {1024 * 8 * size * speed / 60}')
elif command == 's':
    print(f'Square is {1024 * 8 * size * speed / 60 / 60}')
