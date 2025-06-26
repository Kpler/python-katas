def test_compare_hands():
    from poker.compare_hands import compare_hands
    from poker.card import Card, Face, Suit

    # GIVEN
    hand1 = [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]

    hand2 = [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]

    # WHEN
    result = compare_hands(hand1, hand2)

    # THEN
    assert result == "Hand 1 wins"  # Adjust based on actual implementation logic