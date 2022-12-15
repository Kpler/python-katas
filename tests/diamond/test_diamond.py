import unittest

class TestDiamond(unittest.TestCase):

    def test_print(self):
        input = 'A'
        result = print_diamond(input)


        self.assertEqual('A', result)