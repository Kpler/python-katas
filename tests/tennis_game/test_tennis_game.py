from src.tennis_game.match import Match

import pytest


@pytest.fixture
def match():
    return Match()


def test_assure_scores(match):
    allowed_states = ["L", "15", "30", "40", "A"]
    assert match.player1_score in allowed_states
    assert match.player2_score in allowed_states

def test_points_dict(match):
    assert match.player1_score == "L"
    match.player1_points += 1
    assert match.player1_score == "15"
