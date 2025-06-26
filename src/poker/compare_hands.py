from poker.card import Hand, identify_hand

def compare_hands(hand1: Hand, hand2: Hand) -> str:
    hand1_rank = identify_hand(hand1)
    hand2_rank = identify_hand(hand2)
    return [
        {'hand': hand1, 'rank': hand1_rank, 'is_winner': True},
        {'hand': hand2, 'rank': hand2_rank, 'is_winner': False}
    ]
