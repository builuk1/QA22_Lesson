# Инкапсуляция
# Наследование
# Полиморфизм

# Абстракция

# Абстракция <> Конкретика
class Laptop:
    color = 'black'
    CPU = 'i5'
    GPU = 'integr'


class Meat:
    animal = 'pig'
    age = 5


class Steak:
    roast = 'bluerare'


'''Задание 1
Реализуйте класс «Человек». Необходимо хранить в
полях класса: ФИО, дату рождения, контактный телефон,
город, страну, домашний адрес. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса.'''


class Human:
    surname = 'Default'
    name = 'Default'
    second_name = 'Default'
    birth_date = '01.01.1970'
    phone = '+380112223344'
    city = 'Odessa'
    country = 'Ukraine'

    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'ФИО {self.surname} {self.name}'

    def show_phone(self):  # Чтения поля объекта класса
        print(self.phone)

    def change_phone(self, new_phone):  # Записи поля объекта класса
        self.phone = new_phone

    def show_city(self):  # Чтения поля объекта класса
        print(self.city)

    def change_city(self, new_city):  # Записи поля объекта класса
        self.city = new_city


gordon = Human('Freeman', 'Gordon', '+380631234567')
print(gordon)
gordon.show_city()
gordon.show_phone()
gordon.change_city('City17')
gordon.show_city()


class City:
    cityName = ""
    cityRegion = ""
    cityCountry = ""
    population = 0
    mailIndex = 0
    phoneCode = 0

    def __init__(self, Name, Region, Country):
        self.cityName = Name
        self.cityRegion = Region
        self.cityCountry = Country

    def __str__(self):
        return f"Name - {self.cityName}\nRegion - {self.cityRegion}\nCountry - {self.cityCountry}\n" \
               f"Population - {self.population}\nMail index - {self.mailIndex}\nPhone code - {self.phoneCode}\n"

    def setCityName(self, Name):
        self.cityName = Name

    def getCityName(self):
        return self.cityName

    def setCityRegion(self, Region):
        self.cityRegion = Region

    def getCityRegion(self):
        return self.cityRegion

    def setCityCountry(self, Country):
        self.cityCountry = Country

    def getCityCountry(self):
        return self.cityCountry

    def setCityPopulation(self, Population):
        self.population = Population

    def getCityPopulation(self):
        return self.population

    def setCityIndex(self, Index):
        self.mailIndex = Index

    def getCityIndex(self):
        return self.mailIndex

    def setCityCode(self, Code):
        self.phoneCode = Code

    def getCityCode(self):
        return self.phoneCode


Happywile = City("Happywile", "Rainbowland", "Unicornia")
Happywile.setCityPopulation(666)
Happywile.setCityIndex(1)
Happywile.setCityCode(777)
print(Happywile)


class City:
    city_name = 'Empty'
    city_region = 'somewhere'
    city_country = 'Ukraine'
    city_number_of_inhabitants = 1000000
    city_postal_code = 67500
    city_telephone_code = '+80482'

    def __init__(self, city_name, city_country, city_postal_code):
        self.city_name = city_name
        self.city_country = city_country
        self.city_postal_code = city_postal_code

    def __str__(self):
        return f'Ваш город {self.city_name} {self.city_country} {self.city_postal_code}'

    def show_region(self):
        print(self.city_region)

    def change_region(self, new_region):
        self.city_region = new_region

    def show_number_of_inhabitants(self):
        print(self.city_number_of_inhabitants)

    def change_number_of_inhabitants(self, new_number_of_inhabitants):
        self.city_number_of_inhabitants = new_number_of_inhabitants

    def show_telephone_code(self):
        print(self.city_telephone_code)

    def change_telephone_code(self, new_telephone_code):
        self.city_telephone_code = new_telephone_code


gorod = City('Odessa', 'Ukraine', 67511)
print(gorod)

'''Задание 4
Создайте класс «Дробь». Необходимо хранить в полях
класса: числитель и знаменатель. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к
отдельным полям через методы класса. Также создайте
методы класса для выполнения арифметических операций 
(сложение, вычитание, умножение, деление, и т.д.).'''


class Fraction:
    numerator = '12345'
    denominator = '6789'

    def __init__(self, fraction):
        numerator, denominator = fraction.split('/')
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def add(self, other_fraction):  # 5/4
        other_num, other_de = other_fraction.split('/')
        other_num = int(other_num)
        other_de = int(other_de)
        if self.denominator == other_de:
            self.numerator = self.numerator + other_num


platform1 = Fraction('3/4')
print(platform1)
platform1.add('5/4')
print(platform1)


# ***
class Tax:
    total = Fraction('1/2')

    def do_something(self, some):
        print(f'SOME : {some}')


me = Tax()
me.do_something(platform1)


class Buttons:
    exit = 'exit'
    start = 'start'
    de = '1234kdhfe'


button1 = Buttons()

button1.start
button1.de
