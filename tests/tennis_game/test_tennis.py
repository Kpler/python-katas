from src.tennis_game.tennis import Game


def test_init_game():
    game = Game()
    assert game.score == 'love-love'


def test_player1_scoring():
    game = Game()
    game.ball_result(player=1)
    assert game.score == '15-love'
