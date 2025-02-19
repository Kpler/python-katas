from src.texas_holdem.card import Card, Suits, Ranks


def read_card(text: str) -> Card:
    return Card(suit=Suits.CLUBS, rank=Ranks.KING)
