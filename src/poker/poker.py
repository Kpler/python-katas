from poker.with_read_input.poker import HandRank

# We assume that there's exactly 1 winner
def compute_winner_index(hands: list[HandRank]) -> int:
    indexed_hands = enumerate(hands)
    hands_sorted_by_strength_descending = sorted(indexed_hands, key=lambda hand: hand[1], reverse=True)
    winning_hand = hands_sorted_by_strength_descending[0]
    winning_hand_index = winning_hand[0]
    return winning_hand_index

