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

    match.add_point_to_player1()
    assert match.player1_points == 1
    assert match.player1_score == "15"

    match.add_point_to_player1()
    assert match.player1_points == 2
    assert match.player1_score == "30"

    match.add_point_to_player1()
    assert match.player1_points == 3
    assert match.player1_score == "40"

def test_game_win_condition(match):
    match.add_point_to_player1()
    match.add_point_to_player1()
    match.add_point_to_player1()
    match.add_point_to_player1()
    match.check_game_status()
    assert match.winner == "player1"

def test_game_deuce_condition(match):
    match.player1_points = 4
    match.player2_points = 4
    match.check_game_status()
    assert match.winner == "player1"

