# '''Задание 1
# Выведите на экран надпись Nothing will work unless
# you do на разных строках. Пример вывода:
#             Nothing
#             will work
#             unless you do.'''
# a = '        Nothing\n        will work\n        unless you do.\n'
# b = '\t\tNothing\n\t\twill work\n\t\tunless you do.\n'
# print(a)
# print(b)
#
# print(a+b+a+a+b+a)
# '''Задание 2
# Выведите на экран надпись " Anyone who stops learning
# is old, whether at twenty or eighty" Henry Ford на разных
# строках. Пример вывода:
# “Anyone who
#         stops
#                 learning is old,
#                     whether at twenty or eighty”.
#                                         Henry Ford'''
#
# c = '''“Anyone who\n\tstops\n\t\tlearning is old,\n\t\t\twhether at twenty or eighty”.\n\t\t\t\tHenry Ford\n'''
# print(c)
# '''Задание 3
# Пользователь вводит с клавиатуры два числа. Необходимо найти сумму чисел, разницу чисел, произведение
# числе. Результат вычислений вывести на экран.'''
# number1 = float(input("Enter your number1 : "))
# number2 = float(input("Enter your number2 : "))
# print(f'----Calculator----\n'
#       f'{number1} + {number2} = {number1+number2}\n'
#       f'{number1} - {number2} = {number1-number2}\n'
#       f'{number1} * {number2} = {number1*number2}\n'
#       f'{number1} / {number2} = {number1/number2}\n'
#       f'{number1} // {number2} = {number1//number2}\n'
#       f'{number1} % {number2} = {number1%number2}\n'
#       f'{number1} ** {number2} = {number1**number2}')
#
# '''Задание 4
# Пользователь вводит с клавиатуры два числа. Первое
# число — это значение, второе число процент, который
# необходимо посчитать. Например, мы ввели с клавиатуры
# 50 и 10. Требуется вывести на экран 10 процентов от 50.
# Результат: 5'''
# number1 = float(input("Enter your number1 : "))
# number2 = float(input("Enter your number2 : "))
# percentage = (number1/100)*number2
# print(percentage)
# '''Задание 5
# Напишите программу, вычисляющую площадь прямоугольника. Пользователь с клавиатуры вводит ширину
# и высоту прямоугольника.'''
# width = float(input("Enter your width : "))
# height = float(input("Enter your height : "))
# square_of_rectangle = (width * height)/2

'''Задание 1
Пользователь с клавиатуры вводит двухзначное число. Например, 26.
Нужно показать на разных строках
значение первого и второго разряда. В нашем случае это
будет выглядеть так:
2
6'''
# number = int(input("Enter XX number : "))
# n1 = number // 10
# n2 = number % 10
# print(n1, n2, sep='\n')

# '''Задание 2
# Пользователь с клавиатуры вводит трёхзначное число.
# Например, 891. Нужно показать на разных строках значение первого, второго и третьего разряда. Также нужно
# показать на отдельной строке сумму этих трёх чисел.
# В нашем случае это будет выглядеть так:
# 8
# 9
# 1
# 18'''
# number = int(input("Enter XXX number : "))
# n1 = number // 100
# n2 = (number // 10) % 10
# n3 = number % 10
# print(n1, n2, n3, n1 + n2 + n3, sep='\n')
#
# n = 5
# n += 5
# print(n)
# '''Задание 3
# Пользователь вводит с клавиатуры две цифры. Необходимо создать число, содержащее эти цифры.
# Например, если с клавиатуры введено 9, 7, тогда нужно сформировать число 97.'''
# number1 = int(input("Enter number1 : "))
# number2 = int(input("Enter number2 : "))
# print((number1*10)+number2)

'''Задание 4
Пользователь вводит с клавиатуры температуру по
шкале Цельсия. Требуется перевести температуру в градусы по Фаренгейту и вывести на экран.'''
degree_celsius = 20
degree_fahrenheit = float(degree_celsius * (9 / 5)) + 32
print(degree_fahrenheit)
"""Задание * 
С клавиатуры вводится шестизначное число
123456   653421"""

sw = '''Star Wars: Knights of the Old Republic (often abbreviated KOTOR or KotOR) is a role-playing video game set in the Star Wars universe. Developed by BioWare and published by LucasArts, the game was released for the Xbox on July 19, 2003, and for Microsoft Windows on November 19, 2003. The game was later ported to Mac OS X, iOS, and Android by Aspyr, and it is playable on the Xbox 360, Xbox One, and Xbox Series X and Series S via their respective backward compatibility features. A Nintendo Switch version was released on November 11, 2021.

The story of Knights of the Old Republic takes place almost 4,000 years before the formation of the Galactic Empire, where Darth Malak, a Dark Lord of the Sith, has unleashed a Sith armada against the Galactic Republic. The player character, as a Jedi, must venture to different planets in the galaxy to defeat Malak. Players choose from three character classes (Scout, Soldier or Scoundrel) and customize their characters at the beginning of the game, and engage in round-based combat against enemies. Through interacting with other characters and making plot decisions, players can earn Light Side and Dark Side Points, and the alignment system will determine whether the player's character aligns with the light or dark side of the Force.

The game was directed by Casey Hudson, designed by James Ohlen, and written by Drew Karpyshyn. LucasArts proposed developing a game tied to Star Wars: Episode II – Attack of the Clones, or a game set thousands of years before the prequels. The team chose the latter as they thought that they would have more creative freedom. Ed Asner, Ethan Phillips, and Jennifer Hale were hired to perform voices for the game's characters, while Jeremy Soule composed the soundtrack. Announced in 2000, the game was delayed several times before its release in July 2003.

The game received critical acclaim upon release, with critics applauding the game's characters, story, and sound. It was nominated for numerous awards and is often cited as one of the greatest video games ever made. A sequel, Star Wars: Knights of the Old Republic II – The Sith Lords, developed by Obsidian Entertainment at BioWare's suggestion, was released in 2004. The series' story continued with the 2011 release of Star Wars: The Old Republic, a massively multiplayer online role-playing game developed by BioWare. In September 2021, a remake of the game was announced to be in development by Aspyr for Microsoft Windows and PlayStation 5.'''
print(sw)
