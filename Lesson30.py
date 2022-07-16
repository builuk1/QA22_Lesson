'''https://python-scripts.com/object-oriented-programming-in-python#pros-cons-oop'''


# Инкапсуляция

# class Mobile:
#     CPU = 'Snapdragon'
#     RAM = 2
#     IMEI = 111122223333
#
#     def show_CPU(self):
#         print(self.CPU)
#
#     def __init__(self):
#         self.IMEI = Mobile.IMEI + 1
#         Mobile.IMEI = Mobile.IMEI + 1
#
#
# xiaomi = Mobile()
# iphone = Mobile()
# samsung = Mobile()
# print(xiaomi.IMEI)
# print(iphone.IMEI)
# print(samsung.IMEI)

# IMEI       Public
# _IMEI      Protected
# __IMEI     Privat

class Mobile:
    CPU = 'Snapdragon'
    RAM = 2
    __IMEI = 111122223333  # privat

    def show_CPU(self):
        print(self.CPU)

    def __init__(self):
        self.__IMEI = Mobile.__IMEI + 1
        Mobile.__IMEI = Mobile.__IMEI + 1

    def show_IMEI(self):
        print(self.__IMEI)

    def change_IMEI(self, password, new_imei):
        if password == 'root':
            self.__IMEI = new_imei


xiaomi = Mobile()
iphone = Mobile()
samsung = Mobile()
xiaomi.show_IMEI()
iphone.show_IMEI()
samsung.show_IMEI()

iphone.__IMEI = 111  # Не будет работать
iphone.change_IMEI('root', 0)
xiaomi.show_IMEI()
iphone.show_IMEI()
samsung.show_IMEI()


class Person:
    firstName = ""
    lastName = ""
    birthDate = ""
    __city = ""
    __password = ""

    def getCity(self):
        return Person.__city

    def setCity(self, city):
        Person.__city = city

    def getPassword(self):
        return Person.__password

    def setPassword(self, password):
        Person.__city = password

    def changePassword(self, password, newPassword):
        if Person.__password == password:
            Person.__password = newPassword


class User:
    __Login = "User"
    Password = 1234
    ID = 234
    E_mail = "qwerty@gmail.com"
    __Phone = 1234567

    def change_Login(self, password, new_Login):
        if password == 'qwerty':
            self.__Login = new_Login

    def show_Phone(self):
        print(self.__Phone)

    def __init(self):
        pass

    def __init__(self):
        pass


a = User()


class Person:
    firstName = ""
    lastName = ""
    birthDate = ""
    __city = ""
    __password = ""

    def __init__(self, firstName, lastName, birthDate, city, password):
        Person.firstName = firstName
        Person.lastName = lastName
        Person.birthDate = birthDate
        Person.__city = city
        Person.__password = password

    def __str__(self):
        return f"Name: \t {Person.firstName}\nSurname: {Person.lastName}\nBirth date: {Person.birthDate}\n"

    def getCity(self):
        return Person.__city

    def setCity(self, city):
        Person.__city = city

    def getPassword(self):
        return Person.__password

    def setPassword(self, password):
        Person.__city = password

    def changePassword(self, password, newPassword):
        if Person.__password == password:
            Person.__password = newPassword

    def getFirstName(self):
        return Person.firstName

    def setFirstName(self, name):
        Person.firstName = name

    def getLastName(self):
        return Person.lastName

    def setLastName(self, name):
        Person.lastName = name

    def getBirthDate(self):
        return Person.birthDate

    def setBirthDate(self, date):
        Person.birthDate = date


Stepan = Person("Stepan", "Shevchenko", "1.01.1993", "Kiev", "StepanB1939")
print(Stepan)
