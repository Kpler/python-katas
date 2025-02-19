from src.texas_holdem.input import read_card
from src.texas_holdem.card import Card, Suits, Ranks


def test_read_1_card():
    assert read_card("Kc") == Card(suit=Suits.CLUBS, rank=Ranks.KING)
