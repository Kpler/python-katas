import unittest
from src.gilded_rose.guilded_rose import Item


class MyTestCase(unittest.TestCase):
    def test_something(self):
        i = Item('name', 0, 0)
        assertEquals(i)


if __name__ == '__main__':
    unittest.main()
