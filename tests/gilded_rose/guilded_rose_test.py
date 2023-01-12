from approvaltests import verify_all_combinations

from src.gilded_rose.guilded_rose import GildedRose, Item


def test_gilded_rose_approval_test():
    verify_all_combinations(execute_update_quality, [])


def execute_update_quality(name: str, sell_in : int, quality : int) -> Item:
    items_under_test = [
        Item(name, sell_in, quality)
    ]
    gilded_rose = GildedRose(items_under_test)
    gilded_rose.update_quality()
    return gilded_rose.items[0]
