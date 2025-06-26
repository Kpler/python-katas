from poker.card import Hand, identify_hand

def compare_hands(hand1: Hand, hand2: Hand) -> str:
    hand1_rank = identify_hand(hand1)
    hand2_rank = identify_hand(hand2)
    return f"{hand1_rank} - {hand2_rank}"
