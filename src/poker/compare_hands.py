from typing import TypedDict

from poker.card import Hand, identify_hand

class ComparedHands(TypedDict):
    hand: Hand
    rank: str
    is_winner: bool


ranks_power = {
    "Folded": 0,
    "High Card": 1,
    "Pair": 2,
    "Two Pair": 3,
    "Full House": 4,
}


def compare_ranks(ranks: list[str]) -> int:
    return sorted(range(len(ranks)), key=lambda i: ranks_power[ranks[i]], reverse=True)[0]


def compare_hands(hand1: Hand, hand2: Hand) -> list[ComparedHands]:

    hand1_rank = identify_hand(hand1)
    hand2_rank = identify_hand(hand2)

    return [
        {'hand': hand1, 'rank': hand1_rank, 'is_winner': True},
        {'hand': hand2, 'rank': hand2_rank, 'is_winner': False}
    ]
