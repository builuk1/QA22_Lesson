# try except else finally    исключения
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# a = 4
# b = 2
# print(a/b)
#
#
# a = 4
# b = 'dsdsd'
# try:#Попробовать
#     print(a/b)
# except:#Исключение (голое)
#     print('Oooppsss....')


# a = 4
# b = '0'
# try:#Попробовать
#     print(a/b)
# except ZeroDivisionError:
#     print('Zero error')
# except ValueError:
#     print('Value error')
# except TypeError:
#     print('Type error')
# except BaseException:
#     print('Base')
# except:#Исключение (голое)
#     print('Oooppsss....')

# a = 4
# b = 2
# try:  # Попробовать
#     print(a / b)
# except ZeroDivisionError:
#     print('Zero error')
# except ValueError:
#     print('Value error')
# except TypeError:
#     print('Type error')
# except BaseException:
#     print('Base')
# except:  # Исключение (голое)
#     print('Oooppsss....')
# else:  # Если try сработал без ошибок
#     print('Программа отработал в штатном режиме. Ошибок нет')
# finally:
#     print('Сработае всегда')
#
# # switch case > match
# http_code = "418"
# match http_code:
#     case "200":
#         print("OK")
#     case "404":
#         print("Not Found")
#     case "418":
#         print("I'm a teapot")
#     case _:
#         print("Code not found")
#
# # Варианты условий в Python
# # if
# http_code = "418"
# if http_code == "200":
#     print("OK")
# elif http_code == "404":
#     print("Not Found")
# elif http_code == "418":
#     print("I'm a teapot")
# else:
#     print("Code not found")
#
# # while
# http_code = "418"
# while http_code == "200":
#     print("OK")
#     http_code = ''
# while http_code == "404":
#     print("Not Found")
#     http_code = ''
# while http_code == "418":
#     print("I'm a teapot")
#     http_code = ''
# # while: # как заменить else подумайте сами, возможно ли, не знаю
# #     print("Code not found")
#
# # dictionary
# http_code = "418"
# http_dictionary = {"200": "OK", "404": "Not Found", "418": "I'm a teapot"}  # как быть с else подумайте
# print(http_dictionary[http_code])
#
# # Не чисто, но с else
# http_code = "418"
# http_dictionary = {"200": "OK", "404": "Not Found", "418": "I'm a teapot"}  # как быть с else подумайте
# if http_code in http_dictionary:
#     print(http_dictionary[http_code])
# else:
#     print("Code not found")
#
# # С версии Python 3.10
# # switch case > match case
# http_code = "418"
# match http_code:
#     case "200":
#         print("OK")
#     case "404":
#         print("Not Found")
#     case "418":
#         print("I'm a teapot")
#     case _:  # default case > else
#         print("Code not found")
#

# ООП Полиморфизм
# class Mobile:
#     __imei = 123
#
#     def change_imei(self, new_imei):
#         self.__imei = new_imei
#
#
#     def show_imei(self):
#         print(self.__imei)

# class Mobile:
#     __imei = 123
#
#     #getter
#     @property#декоратор > свойство
#     def imei(self):
#         return self.__imei
#
#     @imei.setter
#     def imei(self,new_imei):
#         self.__imei = new_imei
#
#     @imei.deleter
#     def imei(self):
#         self.__imei = 123
#
# xperia = Mobile()
# print(xperia.imei)
# xperia.imei = 456
# print(xperia.imei)
# del xperia.imei
# print(xperia.imei)


class Mobile:
    __imei = 123

    # getter
    @property  # декоратор > свойство
    def imei(self):
        return self.__imei

    @imei.setter
    def imei(self, new_imei):
        if new_imei % 2 == 0:
            self.__imei = new_imei
        else:
            pass

    @imei.deleter
    def imei(self):
        self.__imei = 123


xperia = Mobile()
print(xperia.imei)
xperia.imei = 457  # 456
print(xperia.imei)
del xperia.imei
print(xperia.imei)


# https://python-scripts.com/object-oriented-programming-in-python

# class Money:
#     banktones = Banknotes()
#     coins = Coins()

# Перегрузка
# Перегрузка методов

class Ship:
    weigth = 10000  # Водоизмещение
    heavy = 5000  # Вес груза

    def take(self, new_heavy):
        if new_heavy + self.heavy > self.weigth:
            print('Can not!!!!')
        else:
            self.heavy = self.heavy + new_heavy


delphi = Ship()
print(delphi.heavy)
delphi.take(3000)
print(delphi.heavy)
delphi.take(2000)
print(delphi.heavy)
delphi.take(1)
print(delphi.heavy)


# Перегрузка операторов
# oruell math
# class oint:
#     number = 0
#
#     def __init__(self, n):
#         self.number = n
#
#     def __str__(self):
#         return f'{self.number}'
#
#     def __add__(self, other):
#         self.number = int(self.number) + int(other.number)
#         return f'{self.number}'
#
#
# two = oint(2)
# another_two = oint(2)
# print(two)
# print(two + another_two)

class oint:
    number = 0

    def __init__(self, n):
        self.number = n

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        self.number = int(self.number) + int(other.number) + 1
        return f'{self.number}'

    def __eq__(self, other):
        return ('YOU CANNOT EQUAL IT')


two = oint(2)
another_two = oint(2)
print(f'{two} + {another_two} = {two + another_two}')
print(two == another_two)

# RPG
