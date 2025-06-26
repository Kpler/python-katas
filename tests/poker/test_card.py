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
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.FOUR, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(2, 'K'), (2, '9')],
         'kickers': ['6', '4', '3']
     }),

    ("test_three_of_a_kind", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.EIGHT, suit=Suit.DIAMONDS)
    ], {
         'combinations': [(3, 'K')],
         'kickers': ['9', '8', '6', '3']
     }),

    ("test_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.FOUR, suit=Suit.DIAMONDS),
        Card(face=Face.SEVEN, suit=Suit.HEARTS)
    ], {
         'combinations': [(2, 'K')],
         'kickers': ['9', '7', '6', '4', '3']
     }),

    ("test_high_card", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.ACE, suit=Suit.HEARTS),
        Card(face=Face.FIVE, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.DIAMONDS),
    ], {
         'combinations': [],
         'kickers': ['T', 'K', 'A', '9', '6', '5', '3']
     }),
]

@pytest.mark.parametrize("name, hand, expected", test_data)
def test_get_similar_cards(name, hand, expected):
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
    ("test_folded_2_cards", [
        Card(face=Face.NINE, suit=Suit.HEARTS),
        Card(face=Face.FIVE, suit=Suit.SPADES),
    ], "Folded"),
    ("test_two_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.TWO, suit=Suit.HEARTS)
    ], "Two Pair"),
    ("test_three_of_a_kind", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.EIGHT, suit=Suit.HEARTS)
    ], "Three of a Kind"),

    ("test_pair", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.FIVE, suit=Suit.HEARTS),
        Card(face=Face.SEVEN, suit=Suit.DIAMONDS)
    ], "Pair"),

    ("test_high_card", [
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.FOUR, suit=Suit.SPADES),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.DIAMONDS),
        Card(face=Face.SEVEN, suit=Suit.HEARTS),
    ], "High Card"),
    ("test_straight", [
        Card(face=Face.FIVE, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.SIX, suit=Suit.SPADES),
        Card(face=Face.SEVEN, suit=Suit.DIAMONDS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.DIAMONDS),
        Card(face=Face.TEN, suit=Suit.HEARTS),
    ], "Straight"),
    ("test_flush", [
        Card(face=Face.FOUR, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.CLUBS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SEVEN, suit=Suit.CLUBS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.HEARTS),
    ], "Flush"),
    ("test_straight_flush", [
        Card(face=Face.FOUR, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.CLUBS),
        Card(face=Face.SEVEN, suit=Suit.CLUBS),
        Card(face=Face.EIGHT, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.HEARTS),
    ], "Straight Flush"),
    ("test_royal_flush", [
        Card(face=Face.ACE, suit=Suit.CLUBS),
        Card(face=Face.JACK, suit=Suit.CLUBS),
        Card(face=Face.KING, suit=Suit.CLUBS),
        Card(face=Face.QUEEN, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.CLUBS),
        Card(face=Face.TEN, suit=Suit.HEARTS),
        Card(face=Face.NINE, suit=Suit.HEARTS),
    ], "Royal Flush"),
    ("test_four_of_a_kind", [
        Card(face=Face.ACE, suit=Suit.CLUBS),
        Card(face=Face.ACE, suit=Suit.SPADES),
        Card(face=Face.ACE, suit=Suit.DIAMONDS),
        Card(face=Face.ACE, suit=Suit.HEARTS),
        Card(face=Face.TEN, suit=Suit.CLUBS),
        Card(face=Face.NINE, suit=Suit.SPADES),
        Card(face=Face.SEVEN, suit=Suit.CLUBS),
    ], "Four of a Kind"),
    ("test flush and pair", [
        Card(face=Face.FOUR, suit=Suit.DIAMONDS),
        Card(face=Face.TWO, suit=Suit.DIAMONDS),
        Card(face=Face.KING, suit=Suit.SPADES),
        Card(face=Face.KING, suit=Suit.DIAMONDS),
        Card(face=Face.NINE, suit=Suit.DIAMONDS),
        Card(face=Face.THREE, suit=Suit.CLUBS),
        Card(face=Face.SIX, suit=Suit.DIAMONDS)
    ], "Flush"),
]
@pytest.mark.parametrize("name, hand, expected", test_data_identify_hand)
def test_identify_hand(name, hand, expected):
    assert identify_hand(hand) == expected
