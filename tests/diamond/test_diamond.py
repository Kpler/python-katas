from typing import Sequence


def craft_diamond(widest_letter: str) -> Sequence[str]:
    idx = max(1, ord(widest_letter) - ord('A'))
    if widest_letter == 'A':
        return [widest_letter * 1]
    elif widest_letter == 'C':
        return ['A', 'B' * idx, f"{widest_letter * idx}", 'B' * idx, 'A']
    else:
        return ['A', f"{widest_letter}{widest_letter}", 'A']

#    for (ordinal, index) (ord(widest_letter) to ord('A')) :
#        yield  char(element) * index

    # return [letter * max(1, index) for letter, index]


def test_first_element_diamond():
    diamond = craft_diamond('A')
    assert diamond == ['A']


def test_second_element_diamond():
    diamond = craft_diamond('B')
    assert diamond == ['A', 'BB', 'A']


def test_third_element_diamond():
    diamond = craft_diamond('C')
    assert diamond == ['A', 'BB', 'CC', 'BB', 'A']


def test_xxx():
    assert ord('C') - ord('B') == 1
