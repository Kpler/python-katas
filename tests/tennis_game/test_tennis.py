from src.tennis_game.tennis_game import TennisGame


def test_initial_state() -> None:
    """Test that the initial state of the game is correct."""

    game = TennisGame()
    assert game.player1_score == 0
    assert game.player2_score == 0

    assert game.score() == "love-love"
