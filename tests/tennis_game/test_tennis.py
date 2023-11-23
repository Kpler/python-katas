from src.tennis_game.tennis_game import TennisGame


def test_initial_state() -> None:
    """Test that the initial state of the game is correct."""
    game = TennisGame()
    assert game.scores[0] == 0
    assert game.scores[1] == 0
    assert game.score() == "love-love"


def test_player1_score() -> None:
    game = TennisGame()
    game.register_ball_winner(player=1)
    assert game.scores[0] == 1
    assert game.scores[1] == 0
    assert game.score() == "15-love"


def test_player2_score() -> None:
    game = TennisGame()
    game.register_ball_winner(player=2)
    assert game.scores[0] == 0
    assert game.scores[1] == 1
    assert game.score() == "love-15"
