# '''https://python-scripts.com/object-oriented-programming-in-python'''
#
# s = str('Hello World!')
# l = list()
# l = [1,2,3]
# l.append(4)
#
# class Square:#Чертёж, инструкция, рекомендация к действию
#     color = 'red'#Поле класса, аргумент класса, атрибут класса, переменные класса, то где можем хранить информацию/состояни, имя должно отвечать на вопрос, что, какой сколько
#     def show_color(self):#метод класса, функции класса, то, что может выполнять действие, название глагол, что подразумевает действие
#         print(self.color)
#
# four = Square()
# four.show_color()

class Pen:
    color = 'blue'
    size_of_ball = 0.1
    length = 10
    auto = False
    type = 'ball'


euromax = Pen()
print(euromax.color)
euromax.color = 'green'
print(euromax.color)
bic = Pen()
print(bic.color)


# print(euromax.color)
# print(euromax.color)
# print(euromax.color)
# linter > flake8
# class Borsch:
#     value = 5.0
#     color = 'red'
#     ingredients = ['potato', 'beet', 'onion', 'cabbage', 'pork']
#
#     def take(self):
#         print('You take borsch')
#
#     def add_salt(self):
#         print('You add salt')
#
#     def boiled(self):
#         print('You boiled your plate')
#
#
# my_borsch = Borsch()
# my_borsch.take()
# my_borsch.boiled()
# my_borsch.add_salt()

class Borsch:  # Класс
    value = 5.0  # Поле класса
    color = 'red'
    ingredients = ['potato', 'beet', 'onion', 'cabbage', 'pork']

    def __init__(self, toping, sauce):  # Как будет вести себя объект в момент создания =
        self.toping = toping  # Поле объекта класса, атрибут экземпляра
        self.sauce = sauce

    def __str__(self):  # Как будет вести себя объект при обращении к нему как к строке print()
        return f'V={self.value}, Color : {self.color}'

    def take(self):  # метод класса
        print('You take borsch')

    def add_salt(self):
        print('You add salt')

    def boiled(self):
        print('You boiled your plate')


my_borsch = Borsch('sour_cream', 'garlic')
my_borsch.take()
my_borsch.boiled()
my_borsch.add_salt()
print(my_borsch.toping)
print(my_borsch.sauce)

south_borsch = Borsch('honey', 'fat')
south_borsch.take()
south_borsch.boiled()
south_borsch.add_salt()
print(south_borsch.toping)
print(south_borsch.sauce)

print(my_borsch)
print(south_borsch)

s = str('Hello')
print(s)

show = str(my_borsch)
print(show)
