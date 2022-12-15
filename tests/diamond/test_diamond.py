import io
import unittest
from contextlib import redirect_stdout

from src.diamond.diamond import print_diamond, build_diamond


class TestDiamond(unittest.TestCase):

    def test_print_diamond(self):
        input = 'A'
        f = io.StringIO()
        with redirect_stdout(f):
            print_diamond(input)
        redirected_stdout = f.getvalue().strip()

        self.assertEqual('A', redirected_stdout)



    def test_build_diamond(self):
        input = 'A'
        diamond = build_diamond(input)
        
        self.assertEqual('A', diamond)

    def test_build_diamond_b(self):
        input = 'B'
        diamond = build_diamond(input)

        self.assertEqual(' A \nB B\n A ', diamond)



'''
Input: B
        A
    B       B
        A
'''