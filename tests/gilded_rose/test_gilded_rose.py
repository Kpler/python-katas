from approvaltests.combination_approvals import verify_all_combinations

from src.gilded_rose.guilded_rose import Item, GildedRose


def fn_1(var_1: int, var_2: int) -> int:
    return 9091 * var_1 * var_2


def _execute_gilded_rose_update_quality() -> list[Item]:
    gilded_rose = GildedRose([])
    gilded_rose.update_quality()
    return gilded_rose.items



def test_simple():
    verify_all_combinations(
        fn_1, [list(range(20)), list(range(20))]
    )

def test_gilded_rose():
    verify_all_combinations(
        _execute_gilded_rose_update_quality,
        [],
    )
