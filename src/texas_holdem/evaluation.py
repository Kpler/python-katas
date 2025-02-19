from enum import Enum
from operator import countOf
from collections import Counter
from src.texas_holdem.card import Card


class Evaluation(Enum):
    FOLDED = 0
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3


def evaluate_after_river(cards: list[Card]):
    # After the river,
    # only players with 7 cards are still in the game.
    # All other hands have already been folded.
    if len(cards) < 7:

        return Evaluation.FOLDED
    rank_counts = Counter([c.rank for c in cards])

    combi_counts = Counter([rank_count[1] for rank_count in rank_counts.items()])
    if combi_counts[2] == 1:
        return Evaluation.PAIR
    if combi_counts[2] == 2:
        return Evaluation.TWO_PAIRS
