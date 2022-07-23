# https://docs.pytest.org/en/7.1.x/
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def test_answer1():
    assert inc(3) == 4
