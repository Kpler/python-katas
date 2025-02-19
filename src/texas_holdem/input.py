from src.texas_holdem.card import Card, Suits, Ranks

rank_symbol = {
    "2": Ranks.TWO,
    "3": Ranks.THREE,
    "4": Ranks.FOUR,
    "5": Ranks.FIVE,
    "6": Ranks.SIX,
    "7": Ranks.SEVEN,
    "8": Ranks.EIGHT,
    "9": Ranks.NINE,
    "T": Ranks.TEN,
    "J": Ranks.JACK,
    "Q": Ranks.QUEEN,
    "K": Ranks.KING,
    "A": Ranks.ACE,
}

suit_symbol = {
    "c": Suits.CLUBS,
    "d": Suits.DIAMONDS,
    "h": Suits.HEARTS,
    "s": Suits.SPADES,
}


def read_card(text: str) -> Card:
    return Card(rank=rank_symbol[text[0]], suit=suit_symbol[text[1]])


def read_hand(text: str) -> list[Card]:
    card_inputs = text.strip().split(" ")
    return [read_card(card_input) for card_input in card_inputs]
