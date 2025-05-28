# Texas Holdem

https://codingdojo.org/kata/TexasHoldEm/

## Starter suggestion

Given the subject, you could start by:
```
def test_solve_poker_game() -> None:
    assert solve_poker_game(
        """
        Kc 9s Ks Kd 9d 3c 6d
        9c Ah Ks Kd 9d 3c 6d
        Ac Qc Ks Kd 9d 3c
        9h 5s
        4d 2d Ks Kd 9d 3c 6d
        7s Ts Ks Kd 9d
        """
    ) == """
        Kc 9s Ks Kd 9d 3c 6d Full House (winner)
        9c Ah Ks Kd 9d 3c 6d Two Pair
        Ac Qc Ks Kd 9d 3c 
        9h 5s 
        4d 2d Ks Kd 9d 3c 6d Flush
        7s Ts Ks Kd 9d
    """
```

Then, defining the strategy you would follow to reach the goal. As mentioned in the subject, you will need several steps:
```
def solve_poker_game(input_data: str) -> str:
    hands = parse_input(input_data)
    ranked_hands = rank_hands(hands)
    winner = compute_winner(ranked_hands)
    return format_results(...)
```

## Helpers

You can use the following classes to represent the cards and their properties:
```
from dataclasses import dataclass
from enum import Enum, auto

class Suit(Enum):
    SPADE = auto()
    HEART = auto()
    DIAMOND = auto()
    CLUB = auto()

class Face(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

@dataclass
class Card:
    face: Face
    suit: Suit
```

And you can also use the following mappings:
```
char_to_suit_map = {
    's': Suit.SPADE,
    'h': Suit.HEART,
    'd': Suit.DIAMOND,
    'c': Suit.CLUB
}
char_to_face_map = {
    '2': Face.TWO,
    '3': Face.THREE,
    '4': Face.FOUR,
    '5': Face.FIVE,
    '6': Face.SIX,
    '7': Face.SEVEN,
    '8': Face.EIGHT,
    '9': Face.NINE,
    'T': Face.TEN,
    'J': Face.JACK,
    'Q': Face.QUEEN,
    'K': Face.KING,
    'A': Face.ACE,
```
