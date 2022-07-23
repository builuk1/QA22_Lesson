import pytest
from buyer import *


def test_default_pos():
    assert str(Buyer('John', 'Doe')) == 'John Doe'


def test_welcome_bonus():
    j = Buyer('John', 'Doe')
    assert j.money == 200


def test_buy_50():
    j = Buyer('John', 'Doe')
    j.buy(50)
    assert j.money == 150
