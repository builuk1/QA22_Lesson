# int
# float
# bool
# str

color = 'red'  # str(input("Enter color : "))
pet = 'dog'  # str(input("Enter your pet : "))
# print(color + pet)

number1 = 5
number2 = 2
# print(number1 + number2)

'''*****
   *****
   *****
   *****
   *****'''

s = '*****\n'
p = '|     |\n'
# print(s * 5)
# print(p * 5)

# Ctrl + /    Ctrl + Alt + L      Linter
# str
# str > int
# print(int('5'))
# print(int('dog'))
# str > float
# print(float('5.5'))
# print(float('5'))
# print(float('dog'))
# str > bool
# print(bool('dog'))
# print(bool('true'))
# print(bool('false'))
# print(bool('True'))
# print(bool('False'))
# print(bool(""))

# int
# int > str
# print(str(55) + 'n')
# int > float
# print(float(7)
# int > bool
# print(bool(0))
# print(bool(-5))
# print(bool(5))

# float
# float > int
# print(int(7.8))
# float > str
# print(str(5.5111))
# float > bool
# print(bool(1.0))
# print(bool(0.00000001))
# print(bool(0.0))

# bool
# bool > str
# print(str(True))
# print(str(False))
# bool > int
# print(int(True))
# print(int(False))
# bool > float
# print(float(True))
# print(float(False))

novariablestyle = 1
camelCaseStyle = 2
snake_style_case = 3

# В переменной может быть : в начале
# a-z

# В переменной не желательно использовать : в начале
# A-Z _
# исключение  COUNT = 5  constant
# WIDTH = 800
# HEIGHT = 600

# В переменной не может быть : в начале
# 0-9 а-я !*/ (любые символы, кроме _)


# В переменной может быть : в середине
# a-z 0-9 A-Z _

# В переменной не может быть : в середине
# а-я !*/ (любые символы, кроме _)
# Переменная не может называтся именем, которое является "ключевым словом", список ключевых слов.
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try',
# 'while', 'with', 'yield']

# имя переменной должно быть самоидентифицирующимся

user_separator_in_file = ';'

a = 5  # magic number не понятно что это и откуда взялось

number1 = float(input("Enter your number1 : "))
number2 = float(input("Enter your number2 : "))
print(f'----Calculator----\n'
      f'{number1} + {number2} = {number1 + number2}\n'
      f'{number1} - {number2} = {number1 - number2}\n'
      f'{number1} * {number2} = {number1 * number2}\n'
      f'{number1} / {number2} = {number1 / number2}\n'
      f'{number1} // {number2} = {number1 // number2}\n'
      f'{number1} % {number2} = {number1 % number2}\n'
      f'{number1} ** {number2} = {number1 ** number2}')
# insert меняет тип курсора
