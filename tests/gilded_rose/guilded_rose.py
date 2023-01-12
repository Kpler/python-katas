import unittest
from approvaltests.combination_approvals import verify, verify_all_combinations


# def verify(param):
#     pass
def dumy(input: int, multiply: int):
    return input * multiply


class GettingStartedTest(unittest.TestCase):
    def test_simple(self):
        # verify("Hello ApprovalTests")
        # verify(dumy(2))

        verify_all_combinations(
            dumy, [
                [2, 3, 4],
                [1, 2, 3]
            ]
        )
