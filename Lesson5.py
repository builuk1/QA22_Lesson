# if


# Логические операторы
# >
# <
# >=
# <=
# ==
# !=

# print(5 > 2)
# print(5 > 5)
# print(5 >= 5)
# print(4 < 3)
# print(6 == 6)
# print(4 != 3)
# button = ''
# if True:
#     print('Always work')
#
# if button:
#     print('Sometimes work')
#
# age = 18
# if age < 18:  # True
#     print('You are a child')
# if age >= 18:
#     print('You are an adult')
#
# height = int(input("Enter your height : ")) # граница - 140 см
# if height < 140:
#     print("not allowed on the hills")
# if height >= 140:
#     print("go ride")
#
# age = 18
# if age < 18:  # True
#     print('You are a child')
# else:
#     print('You are an adult')
#
# mark = 5
# if mark < 5:
#     print('You are fail exam')
# else:
#     print('You are pass exam')
#
# #Чуть правильнее. Потому что на синий не пойдёт
# light = str(input("light is: "))
# if light == 'green':
#     print("go")
# else:
#     print("stop")
#
# light = 'red'
# if light == 'red':
#     print("Stop!!!")
# else:
#     print("Go!!!")
#
# age = 13
# if age < 0:
#     print('Error')
# elif age < 18:  # True
#     print('You are a child')
# else:
#     print('You are an adult')

# height = int(input("Enter your height : "))
# if height < 0:
#     print('Error, negative height')
# elif height < 140:
#     print("not allowed on the hills")
# else:
#     print("go ride")

age = 12
if age < 0:
    print('Error -')
elif age < 13:  # True
    print('You are a child')
elif age < 18:  # True
    print('You are a teen')
elif age < 135:  # True
    print('You are an adult')
elif age >= 135:
    print('Error +')
else:
    print("Some error")

# while/ dicitionary альтернатива if

height = int(input("Enter your height : "))
if height < 0:
    print("error -")
elif height < 100:
    print("too small")
elif height < 140:
    print("go child carousel ")
elif height < 220:
    print("go anywhere ")
elif height >= 220:
    print("error +")
else:
    print("Some error")
