from src.texas_holdem.card import Card, Ranks, Suits
from src.texas_holdem.input import read_hand


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


def test_read_with_starting_white_space():
    assert read_hand("  Kc 9s Ks Kd 9d 3c 6d") == [
        Card(rank=Ranks.KING, suit=Suits.CLUBS),
        Card(rank=Ranks.NINE, suit=Suits.SPADES),
        Card(rank=Ranks.KING, suit=Suits.SPADES),
        Card(rank=Ranks.KING, suit=Suits.DIAMONDS),
        Card(rank=Ranks.NINE, suit=Suits.DIAMONDS),
        Card(rank=Ranks.THREE, suit=Suits.CLUBS),
        Card(rank=Ranks.SIX, suit=Suits.DIAMONDS),
    ]
