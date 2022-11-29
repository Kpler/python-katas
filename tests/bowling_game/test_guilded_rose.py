from approvaltests.combination_approvals import verify_all_combinations

from src.gilded_rose.guilded_rose import Item, GildedRose


def test_gilded_rose_approval_tests():
    verify_all_combinations(
        execute_update_quality,
        [['Aged Brie'],
        [1],
        [1]]
    )


def execute_update_quality(name: str, sell_in: int, quality: int) -> Item:
    items_under_test = [
        Item(name=name, sell_in=sell_in, quality=quality),
    ]
    gilded_rose = GildedRose(items_under_test)
    gilded_rose.update_quality()
    return gilded_rose.items[0]
