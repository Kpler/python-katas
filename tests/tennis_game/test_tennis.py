import pytest

from src.tennis_game.tennis import TennisGame, IllegalPlayerException

@pytest.mark.parametrize("scorers, score",
    [([], "love - love"), ([1], "15 - love"), ([1, 1], "30 - love"),
     ([2], "love - 15"), ([1,1,1,1,2,2,2,2], "deuce"), ([1,1,1,2,2,2], "deuce")
    ])
def test_game(scorers, score) -> None:
    # GIVEN
    tennis_game = TennisGame()
    # WHEN
    for s in scorers:
        tennis_game.play(scorer=s)
    # THEN
    assert tennis_game.get_score() == score

def test_game_when_illegal_player() -> None:
    # GIVEN
    tennis_game = TennisGame()
    # WHEN / THEN
    with pytest.raises(IllegalPlayerException):
        tennis_game.play(scorer=3)

