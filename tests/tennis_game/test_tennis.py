from src.tennis_game.tennis import TennisGame, WrongPlayerException
import pytest

@pytest.fixture
def tennis_game() -> TennisGame:
    return TennisGame()

@pytest.mark.parametrize("scorers, score",
    [
        ([], "love - love"),
        ([1], "15 - love"),
        ([2], "love - 15"),
        ([1, 1, 1, 1], "Player 1 Win!"),
        ([2, 2, 2, 2], "Player 2 Win!"),
        ([1, 1, 1, 2, 2, 2], "deuce"),
        ([1, 1, 1, 2, 2, 2, 1], "Advantage 1"),
    ])
def test_game(tennis_game: TennisGame, scorers: list[int], score: str) -> None:
    for s in scorers:
        tennis_game.gain_point(player=s)
    assert tennis_game.get_score() == score

def test_game_score_player_3(tennis_game: TennisGame) -> None:
    with pytest.raises(WrongPlayerException):
        tennis_game.gain_point(3)
