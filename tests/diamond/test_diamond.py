import io
import unittest
from contextlib import redirect_stdout

from src.diamond.diamond import print_diamond


class TestDiamond(unittest.TestCase):

    def test_print(self):
        input = 'A'
        result = print_diamond(input)
        f = io.StringIO()
        with redirect_stdout(f):
            print_diamond(input)
        redirected_stdout = f.getvalue()

        self.assertEqual('A', result)