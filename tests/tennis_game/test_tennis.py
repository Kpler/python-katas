from src.tennis_game.tennis_game import TennisGame
from src.tennis_game.tennis_game import Player


def test_initialise():
    game = TennisGame()
    assert game.score == 'love-love'


def test_player_assume_nominal_scores():
    player = Player()
    assert player.score == 'love'
    player.win_ball()
    assert player.score == '15'
    player.win_ball()
    assert player.score == '30'
    player.win_ball()
    assert player.score == '40'
    player.win_ball()
    assert player.score == 'win'


def test_score_tennis_game_increasing():
    game = TennisGame()
    game.ball_result(1)
    assert game.score == "15-love"
    game.ball_result(1)
    assert game.score == "30-love"
    game.ball_result(1)
    assert game.score == "40-love"
