class Buyer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.money = 200

    def __str__(self):
        return f'{self.name} {self.surname}'

    # def __eq__(self, other): # изначально пыталось сделать это, потому добавили str
    #     pass

    def buy(self, cost):
        self.money = self.money - cost
