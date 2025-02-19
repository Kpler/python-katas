import pytest

from src.texas_holdem.input import read_card, read_hand
from src.texas_holdem.card import Card, Suits, Ranks

testdata = [
    (Card(rank=Ranks.KING, suit=Suits.CLUBS), "Kc"),
    (Card(rank=Ranks.NINE, suit=Suits.SPADES), "9s"),
    (Card(rank=Ranks.KING, suit=Suits.SPADES), "Ks"),
    (Card(rank=Ranks.KING, suit=Suits.DIAMONDS), "Kd"),
    (Card(rank=Ranks.NINE, suit=Suits.DIAMONDS), "9d"),
    (Card(rank=Ranks.THREE, suit=Suits.CLUBS), "3c"),
    (Card(rank=Ranks.SIX, suit=Suits.DIAMONDS), "6d"),
]


@pytest.mark.parametrize("expected, input", testdata)
def test_read_1_card(expected, input):
    assert read_card(input) == expected


# Kc 9s Ks Kd 9d 3c 6d
def test_read_multi_card_hand():
    assert read_hand("Kc 9s Ks Kd 9d 3c 6d") == [
        Card(rank=Ranks.KING, suit=Suits.CLUBS),
        Card(rank=Ranks.NINE, suit=Suits.SPADES),
        Card(rank=Ranks.KING, suit=Suits.SPADES),
        Card(rank=Ranks.KING, suit=Suits.DIAMONDS),
        Card(rank=Ranks.NINE, suit=Suits.DIAMONDS),
        Card(rank=Ranks.THREE, suit=Suits.CLUBS),
        Card(rank=Ranks.SIX, suit=Suits.DIAMONDS),
    ]
