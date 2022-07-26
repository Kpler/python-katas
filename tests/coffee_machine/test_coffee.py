import unittest


class CoffeeTestCase(unittest.TestCase):
    def test_tea_order(self):
        result = self.make_order(drink_type, sugar)
        self.assertEqual("T:1:0", "T:1:0")  # add assertion here

    def make_order(self, drink_type, sugar):
        return ':'.join(drink_type, sugar)


if __name__ == '__main__':
    unittest.main()
