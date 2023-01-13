from typing import Any

from approvaltests.combination_approvals import verify_all_combinations

from src.gilded_rose.guilded_rose import Item, GildedRose


def fn_1(var_1: int, var_2: int) -> int:
    return 9091 * var_1 * var_2


def _execute_gilded_rose_update_quality(
    names: list[Any], sell_ins: list[Any], qualities: list[Any]
) -> list[Item]:
    items = [
        Item(name=name, sell_in=sell_in, quality=quality)
        for name, sell_in, quality in zip(names, sell_ins, qualities)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return gilded_rose.items


def test_simple():
    verify_all_combinations(
        fn_1, [list(range(20)), list(range(20))]
    )


def test_gilded_rose():
    names = ["foobar", "random", 123]
    sell_ins = ["sell_in", 1, 888]
    qualities = ["good", 1, 789]

    verify_all_combinations(_execute_gilded_rose_update_quality, [names, sell_ins, qualities])
