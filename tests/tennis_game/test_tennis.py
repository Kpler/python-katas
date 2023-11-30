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