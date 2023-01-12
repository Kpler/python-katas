import unittest
from typing import List

from approvaltests.combination_approvals import verify_all_combinations

from src.gilded_rose.guilded_rose import Item, GildedRose


def dumy(input: int, multiply: int):
    return input * multiply


def _execute_gilded_rose(names: List[str], sell_ins: List[int], qualities: List[int]) -> List[Item]:

    items = []
    for name in names:
        for sell_in in sell_ins:
            for quality in qualities:
                items.append(Item(name=name, sell_in=sell_in, quality=quality))

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return gilded_rose.items


class GildedRoseTest(unittest.TestCase):
    def test_gilded_rose(self):

        possible_values_for_names = [[], ["unknown"], ["Aged Brie", "unknown"]]
        possible_values_for_sellins_or_qualities = [[0], [0, 1], [0, 50, 101], [0, 1, 2, 51]]

        verify_all_combinations(
            _execute_gilded_rose, [
                possible_values_for_names,
                possible_values_for_sellins_or_qualities,
                possible_values_for_sellins_or_qualities,
            ]
        )
