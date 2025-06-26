from enum import Enum
from typing import List, Tuple, Dict
from dataclasses import dataclass
from collections import Counter

from collections import Counter

class Suit(Enum):
    CLUBS = 'c'
    DIAMONDS = 'd'
    HEARTS = 'h'
    SPADES = 's'

class Face(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


face_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

@dataclass
class Card:
    face: Face
    suit: Suit

Hand = List[Card]


def parse_cards(input_line: str) -> Hand:
    face_map = {face.value: face for face in Face}
    suit_map = {suit.value: suit for suit in Suit}
    cards = input_line.split()
    return [Card(face=face_map[card[0]], suit=suit_map[card[1]]) for card in cards]


def get_similar_cards(hand: Hand) -> Dict[str, List]:
    faces = [card.face for card in hand]
    face_counts = Counter(faces)
    combinations_set = set()
    for face, count in face_counts.items():
        if count > 1:
            combinations_set.add((count, face.value))
    combinations = sorted(combinations_set, reverse=True)

    kickers = sorted([face.value for face in faces if face_counts[face] == 1], reverse=True)

    return {
        'combinations': combinations,
        'kickers': kickers
    }


def is_flush(hand: List[Card]) -> bool:
    suits = [card.suit for card in hand]

    suit_counts = Counter(card.suit for card in hand)
    return any(count >= 5 for count in suit_counts.values())
    #return len(set(suits)) == 1

def is_straight(hand: List[Card]) -> Tuple[bool, int]:
    faces = sorted([face_values[card.face.value] for card in hand])
    unique_faces = list(sorted(set(faces)))

    if len(unique_faces) < 5:
        return False, 0

    for i in range(len(unique_faces) - 5, -1, -1):
        if unique_faces[i:i+5] == list(range(unique_faces[i], unique_faces[i]+5)):
            return True, unique_faces[i+4]
    # specific case with ace when we have a low straight
    if set(unique_faces) >= {2, 3, 4, 5, 14}:
        return True, 5

    return False, 0

def is_royal_flush(hand: List[Card]) -> bool:
    is_flush_hand = is_flush(hand)
    is_straight_hand, high_card = is_straight(hand)
    return is_flush_hand and is_straight_hand and high_card == 14



def identify_hand(hand: Hand) -> str:
    hand_ranks = get_similar_cards(hand)
    combinations = hand_ranks['combinations']
    flush = is_flush(hand)
    straight, high_card = is_straight(hand)

    if len(hand) < 7:
        return "Folded"
    if is_royal_flush(hand):
        return "Royal Flush"
    elif straight and flush:
        return "Straight Flush"
    elif combinations and combinations[0][0] == 4:
        return "Four of a Kind"
    elif len(combinations) == 2 and combinations[0][0] == 3 and combinations[1][0] == 2:
        return "Full House"
    elif flush and not straight:
        return "Flush"
    elif straight and not flush:
        return "Straight"
    elif len(combinations) == 2 and combinations[0][0] == 2 and combinations[1][0] == 2:
        return "Two Pair"
    elif len(combinations) == 1 and combinations[0][0] == 3:
        return "Three of a Kind"
    elif len(combinations) == 1 and combinations[0][0] == 2:
        return "Pair"
    else:
        return "High Card"