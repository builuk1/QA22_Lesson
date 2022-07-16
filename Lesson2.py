# name = str(input("Enter your name : "))  # Linter Flake8 проверка правописания в проекте
# age = int(input("Enter your age : "))
# height = float(input("Enter your height : "))
# is_student = bool(input("Enter you are a student : "))
# print(name, age, height, is_student)
# #Задание * как убрать "age is 28 . My " пробел перед точкой в первом случае
# print("My name is", name, "and my age is", age, ". My height is", height, "and I am student", is_student)#основан на методах print'а, не работает вне консоли
# print("My name is "+str(name)+" and my age is "+str(age)+" . My height is "+str(height)+" and I am student "+str(is_student))#Основан на конкантенации ( соединении ) строк
# print("My name is {} and my age is {} . My height is {} and I am student {}".format(name, age, height, is_student))#Python до 3.6, позже тоже, но есть методы лучше
# print(f"My name is {name} and my age is {age} . My height is {height} and I am student {is_student}")

# Ctrl + / комментирование выделенной строки
number1 = 7
number2 = 5
print(number1 + number2)
number3 = (number1 + number2) * number1
print(number3)
# Математические операторы
print(number1 + number2)  # + оператор   number1 и number2 операнды    оператор бинарный
print(number1 - number2)  # -number1 унарный оператор минус
print(number1 * number2)
print(number1 / number2)  # деление
print(number1 // number2)  # целочисленное деление
print(number1 % number2)  # остаток от деления
print(number1 ** number2)  # возведение первого числа, в степень второго

a = 30  # int(input("Enter your age : "))
b = 42  # int(input("Enter your age : "))
c = 5
print((a + b + c) / 3)
print(4 / 2)
print(f'({a} + {b} + {c}) / 3 = {(a + b + c) / 3}')
# S = a × b
# 12 = 3 x 4
