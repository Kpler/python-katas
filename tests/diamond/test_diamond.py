from typing import Sequence

import pytest as pytest


def craft_diamond(widest_letter: str) -> Sequence[str]:
    if widest_letter == 'A':
        return [widest_letter]
    else:
        return ['A', f"{widest_letter}{widest_letter}", 'A']


def test_single_element_diamond():
    diamond = craft_diamond('A')
    assert diamond == ['A']


def test_two_elements_diamond():
    diamond = craft_diamond('B')
    assert diamond == ['A', 'BB', 'A']
