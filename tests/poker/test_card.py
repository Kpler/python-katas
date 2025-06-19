import pytest

from src.poker.card import Face, Suit, Hand, Card, parse_cards, identify_hand, get_similar_cards


def test_parse_cards():
    input_line = "Kc 9s Ks Kd 9d 3c 6d"
    expected = [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]
    assert parse_cards(input_line) == expected





test_data = [
    ("test_full_house", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(3, 'K'), (2, '9')],
         'kickers': ['6', '3']
     }),

    ("test_two_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(2, 'K'), (2, '9')],
         'kickers': ['6', '3']
     }),

    ("test_three_of_a_kind", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(3, 'K')],
         'kickers': ['9', '6', '3']
     }),

    ("test_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(2, 'K')],
         'kickers': ['9', '6', '3']
     }),

    ("test_high_card", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], {
         'combinations': [],
         'kickers': ['K', '9', '6', '3']
     }),
]

@pytest.mark.parametrize("name, hand, expected", test_data)
def test_get_hand_ranks(name, hand, expected):
    assert get_similar_cards(hand) == expected



def test_identify_hand():
    hand = [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ]
    assert identify_hand(hand) == "Full House"


test_data_identify_hand = [
    ("test_full_house", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "Full House"),

    ("test_two_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "Two Pair"),

    ("test_three_of_a_kind", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "Three of a Kind"),

    ("test_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "Pair"),

    ("test_high_card", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "High Card"),
    ("test_straight", [
        Card(face=Face.FIVE, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.SIX, suit=Suit.SPADES),
        Card(face=Face.SEVEN, suit=Suit.DIAMONDS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.DIAMONDS)
    ], "Straight"),
    ("test_flush", [
        Card(face=Face.FOUR, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.CLUBS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SEVEN, suit=Suit.CLUBS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS)
    ], "Flush"),
    ("test_straight_flush", [
        Card(face=Face.FOUR, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.CLUBS),
        Card(face=Face.SEVEN, suit=Suit.CLUBS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS)
    ], "Straight Flush"),
    ("test_royal_flush", [
        Card(face=Face.ACE, suit=Suit.CLUBS),
        Card(face=Face.JACK, suit=Suit.CLUBS),
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.QUEEN, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS)
    ], "Royal Flush"),
    ("test_four_of_a_kind", [
        Card(face=Face.ACE, suit=Suit.CLUBS),
        Card(face=Face.ACE, suit=Suit.SPADES),
        Card(face=Face.ACE, suit=Suit.DIAMONDS),
        Card(face=Face.ACE, suit=Suit.HEARTS),
        Card(face=Face.TEN, suit=Suit.CLUBS)
    ], "Four of a Kind"),
]
@pytest.mark.parametrize("name, hand, expected", test_data_identify_hand)
def test_identify_hand(name, hand, expected):
    assert identify_hand(hand) == expected