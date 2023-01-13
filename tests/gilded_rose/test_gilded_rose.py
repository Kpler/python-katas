from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations


def fn_1(var_1: int, var_2: int) -> int:
    return 9091 * var_1 * var_2


def test_simple():
    verify_all_combinations(
        fn_1, [list(range(20)), list(range(20))]
    )
