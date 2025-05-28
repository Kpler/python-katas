from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto

class Suit(Enum):
    SPADE = "s"
    HEART = "h"
    DIAMOND = "d"
    CLUB = "c"

class Rank(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "T"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

class HandRankType(Enum):
    HIGH_CARD = 0
    PAIR = 1
    FOLDED = -1

RANK_ORDER = tuple(r for r in Rank)


@dataclass
class Card:
    rank: Rank
    suit: Suit
    
    @classmethod
    def from_str(cls, card_string: str) -> Card:
        rank, suit = card_string
        return Card(rank=Rank(rank), suit=Suit(suit))

    def __gt__(self, other):
        return RANK_ORDER.index(self.rank) > RANK_ORDER.index(other.rank)

@dataclass
class HandRank:
    type: HandRankType
    values: list[Rank]


def read_input(input_str: str) -> list[list[Card]]:
    hands = input_str.split('\n')
    return [
        [Card.from_str(card) for card in hand.strip().split(' ')] for hand in hands
    ]


def rank_hand(hand: list[Card]) -> HandRank:
    values = [card.rank for card in reversed(sorted(hand))]
    if (values[0] == values[1]):
        return HandRank(
            type=HandRankType.PAIR,
            values=values,
        )
    return HandRank(
        type=HandRankType.HIGH_CARD,
        values=values,
    )
