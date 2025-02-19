from src.texas_holdem.card import Card, Ranks, Suits
from src.texas_holdem.evaluation import Evaluation, evaluate_after_river


def test_not_enough_cards():
    assert (
        evaluate_after_river(
            [Card(rank=Ranks.SEVEN, suit=Suits.DIAMONDS), Card(rank=Ranks.TWO, suit=Suits.HEARTS)]
        )
        == Evaluation.FOLDED
    )
