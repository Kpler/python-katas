from poker.compare_hands import compare_hands
from poker.card import Card, Face, Suit

def test_compare_hands():
    # GIVEN
    hand1 = [ #Kc 9s Ks Kd 9d 3c 6d Full House
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]

    hand2 = [ #9c Ah Ks Kd 9d 3c 6d
        Card(face=Face.NINE, suit=Suit.CLUBS),
        Card(face=Face.ACE, suit=Suit.HEARTS),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS)

    ]

    # WHEN
    result = compare_hands(hand1, hand2)

    # THEN
    assert result == [
        {'hand': hand1, 'rank': "Full House", 'is_winner': True},
        {'hand' : hand2, 'rank': "Two Pair", 'is_winner': False},
    ]

def test_compare_hands_2():
    # GIVEN
    hand1 = [ #4d 2d Ks Kd 9d 3c 6d Flush
        Card(face=Face.FOUR, suit=Suit.DIAMONDS),
        Card(face=Face.TWO, suit=Suit.DIAMONDS),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]

    hand2 = [ #9c 5s
        Card(face=Face.NINE, suit=Suit.HEARTS),
        Card(face=Face.FIVE, suit=Suit.SPADES),

    ]

    # WHEN
    result = compare_hands(hand1, hand2)

    # THEN
    assert result == [
        {'hand': hand1, 'rank': "Flush", 'is_winner': True},
        {'hand' : hand2, 'rank': "Folded", 'is_winner': False},
    ]

