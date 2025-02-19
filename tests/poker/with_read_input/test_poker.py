from poker.with_read_input.poker import *
import pytest

king_of_spade = Card(rank=Rank.KING, suit=Suit.SPADE)
nine_of_diamond = Card(rank=Rank.NINE, suit=Suit.DIAMOND)
nine_of_spade = Card(rank=Rank.NINE, suit=Suit.SPADE)
ace_of_club = Card(rank=Rank.ACE, suit=Suit.CLUB)

@pytest.mark.parametrize(
    "input,expected",
    [
        ('Ks', [[king_of_spade]]),
        ('Ks\n9d', [[king_of_spade], [nine_of_diamond]]),
        ('Ks 9d\nAc 9d', [[king_of_spade,nine_of_diamond], [ace_of_club,nine_of_diamond]]),
        ('  Ks  ', [[king_of_spade]]),
    ]
)
def test_read_input(input: str, expected: list[list[Card]]) -> None:
    result = read_input(input)
    assert result == expected

@pytest.mark.parametrize(
    "hand,expected",
    [
        ([king_of_spade, nine_of_diamond], HandRank(type=HandRankType.HIGH_CARD, values=[Rank.KING, Rank.NINE])),
        ([nine_of_diamond, king_of_spade], HandRank(type=HandRankType.HIGH_CARD, values=[Rank.KING, Rank.NINE])),
        ([nine_of_diamond, nine_of_spade], HandRank(type=HandRankType.PAIR, values=[Rank.NINE, Rank.NINE])),
    ]
)
def test_rank_hand(hand: list[Card], expected: HandRank):
    result = rank_hand(hand)
    assert result == expected
