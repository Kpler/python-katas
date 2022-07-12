import pytest


def make_new_order():
    pass


from dataclasses import dataclass
import typing


@dataclass
class Drinkorder:
    drink_type: str
    num_sugar: int
    stick: int


def test_new_order():
    assert make_new_order(Drinkorder("T", 1, 0)) == "T:1:0"
