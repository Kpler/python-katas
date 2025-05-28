from poker.poker import compute_winner
from poker.with_read_input.poker import HandRank, HandRankType

player_one_hand = HandRank(type=HandRankType.HIGH_CARD, values=[])
folded_hand = HandRank(type=HandRankType.FOLDED, values=[])

def test_compute_winner_when_only_one_player() -> None:
    # GIVEN a list of hands where there is only one hand
    hands = [
        player_one_hand
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner(hands)
    # THEN the winner index should be 0
    assert winner_index == 0


def test_compute_winner_when_two_players_and_one_folded() -> None:
    # GIVEN a list of hands where there is only one hand
    hands = [
        folded_hand,
        player_one_hand
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner(hands)
    # THEN the winner index should be 0
    assert winner_index == 1
