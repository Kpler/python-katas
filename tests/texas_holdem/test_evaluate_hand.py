from src.texas_holdem.card import Card, Ranks, Suits
from src.texas_holdem.evaluation import Evaluation, evaluate_after_river


def test_not_enough_cards():
    assert (
        evaluate_after_river(
            [Card(rank=Ranks.SEVEN, suit=Suits.DIAMONDS), Card(rank=Ranks.TWO, suit=Suits.HEARTS)]
        )
        == Evaluation.FOLDED
    )


def test_evaluate_pair():
    cards = [
        Card(Ranks.TWO, Suits.CLUBS),
        Card(Ranks.TWO, Suits.DIAMONDS),  # pair of TWOs
        Card(Ranks.THREE, Suits.HEARTS),
        Card(Ranks.FIVE, Suits.SPADES),
        Card(Ranks.SEVEN, Suits.CLUBS),
        Card(Ranks.NINE, Suits.HEARTS),
        Card(Ranks.KING, Suits.DIAMONDS),
    ]
    assert evaluate_after_river(cards) == Evaluation.PAIR


def test_evaluate_2_pairs():
    cards = [
        Card(Ranks.TWO, Suits.CLUBS),
        Card(Ranks.TWO, Suits.DIAMONDS),  # pair of TWOs
        Card(Ranks.THREE, Suits.HEARTS),
        Card(Ranks.THREE, Suits.SPADES),
        Card(Ranks.SEVEN, Suits.CLUBS),
        Card(Ranks.NINE, Suits.HEARTS),
        Card(Ranks.KING, Suits.DIAMONDS),
    ]
    assert evaluate_after_river(cards) == Evaluation.TWO_PAIRS
