import pytest
from src.tennis.tennis import Tennis, Player, WinningGame


def test_player_1_point() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"


def test_player_1_two_points() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.ONE) == "30-love"


def test_player_1_one_point_player_2_one_point() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"


def test_deuce() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"
    assert tennis.play(Player.ONE) == "30-15"
    assert tennis.play(Player.TWO) == "30-30"
    assert tennis.play(Player.ONE) == "40-30"
    assert tennis.play(Player.TWO) == "deuce"


def test_advantage_player_1() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"
    assert tennis.play(Player.ONE) == "30-15"
    assert tennis.play(Player.TWO) == "30-30"
    assert tennis.play(Player.ONE) == "40-30"
    assert tennis.play(Player.TWO) == "deuce"
    assert tennis.play(Player.ONE) == "advantage one"


def test_advantage_player_2() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"
    assert tennis.play(Player.ONE) == "30-15"
    assert tennis.play(Player.TWO) == "30-30"
    assert tennis.play(Player.ONE) == "40-30"
    assert tennis.play(Player.TWO) == "deuce"
    assert tennis.play(Player.TWO) == "advantage two"


def test_return_to_deuce_from_advantage() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"
    assert tennis.play(Player.ONE) == "30-15"
    assert tennis.play(Player.TWO) == "30-30"
    assert tennis.play(Player.ONE) == "40-30"
    assert tennis.play(Player.TWO) == "deuce"
    assert tennis.play(Player.ONE) == "advantage one"
    assert tennis.play(Player.TWO) == "deuce"


def test_player_1_wins() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.TWO) == "15-15"
    assert tennis.play(Player.ONE) == "30-15"
    assert tennis.play(Player.TWO) == "30-30"
    assert tennis.play(Player.ONE) == "40-30"
    assert tennis.play(Player.TWO) == "deuce"
    assert tennis.play(Player.ONE) == "advantage one"
    assert tennis.play(Player.TWO) == "deuce"
    assert tennis.play(Player.ONE) == "advantage one"
    with pytest.raises(WinningGame):
        tennis.play(Player.ONE)


def test_player_1_wins_shutout() -> None:
    tennis = Tennis()
    assert tennis.play(Player.ONE) == "15-love"
    assert tennis.play(Player.ONE) == "30-love"
    assert tennis.play(Player.ONE) == "40-love"
    with pytest.raises(WinningGame):
        tennis.play(Player.ONE)
