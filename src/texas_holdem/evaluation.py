from enum import Enum
from operator import countOf
from collections import Counter
from src.texas_holdem.card import Card


class Evaluation(Enum):
    FOLDED = 0
    HIGH_CARD = 1
    PAIR = 2


def evaluate_after_river(cards: list[Card]):
    # After the river,
    # only players with 7 cards are still in the game.
    # All other hands have already been folded.
    if len(cards) < 7:

        return Evaluation.FOLDED
    rank_counts = Counter([c.rank for c in cards])
    if any(count == 2 for count in rank_counts.values()):
        return Evaluation.PAIR
