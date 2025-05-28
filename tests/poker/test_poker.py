from poker.poker import compute_winner_index
from poker.with_read_input.poker import HandRank, HandRankType, Rank

high_card_hand_ace_jack_ten = HandRank(type=HandRankType.HIGH_CARD, values=[Rank.ACE, Rank.JACK, Rank.TEN, Rank.SEVEN, Rank.FIVE])
high_card_hand_ace_jack_nine = HandRank(type=HandRankType.HIGH_CARD, values=[Rank.ACE, Rank.JACK, Rank.NINE, Rank.SEVEN, Rank.FIVE])
high_card_hand_jack = HandRank(type=HandRankType.HIGH_CARD, values=[Rank.JACK, Rank.TEN, Rank.NINE, Rank.SEVEN, Rank.FIVE])
folded_hand = HandRank(type=HandRankType.FOLDED, values=[Rank.JACK, Rank.TEN, Rank.NINE, Rank.SEVEN])

def test_compute_winner_when_only_one_player() -> None:
    # GIVEN a list of hands where there is only one hand
    hands = [
        high_card_hand_ace_jack_ten
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner_index(hands)
    # THEN the winner index should be 0
    assert winner_index == 0


def test_compute_winner_when_two_players_and_one_folded() -> None:
    hands = [
        folded_hand,
        high_card_hand_ace_jack_ten,
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner_index(hands)

    assert winner_index == 1

def test_compute_winner_when_two_players_high_cards() -> None:
    hands = [
        high_card_hand_jack,
        high_card_hand_ace_jack_ten,
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner_index(hands)

    assert winner_index == 1


def test_compute_winner_when_two_players_with_different_3rd_card() -> None:
    hands = [
        high_card_hand_jack,
        high_card_hand_ace_jack_ten,
        high_card_hand_ace_jack_nine
    ]
    # WHEN I call compute_winner
    winner_index = compute_winner_index(hands)

    assert winner_index == 1
