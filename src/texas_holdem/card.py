from dataclasses import dataclass
from enum import Enum


class Suits(Enum):
    SPADES = "spades"
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"


class Ranks(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass
class Card:
    rank: Ranks
    suit: Suits

