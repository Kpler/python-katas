from src.tennis_game.tennis import Game


def test_init_game():
    game = Game()
    assert game.score == 'love-love'


def test_player1_scoring():
    game = Game()
    game.ball_result(player=1)
    assert game.score == '15-love'
    game.ball_result(player=1)
    assert game.score == '30-love'
    game.ball_result(player=1)
    assert game.score == '40-love'


def test_player2_scoring():
    game = Game()
    game.ball_result(player=2)
    assert game.score == 'love-15'
    game.ball_result(player=2)
    assert game.score == 'love-30'
    game.ball_result(player=2)
    assert game.score == 'love-40'


def test_win_player_1():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)

    assert game.score == "Player 1 wins"

def test_win_player_2():
    game = Game()
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)

    assert game.score == "Player 2 wins"

def test_deuce():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)

    assert game.score == "deuce"

def test_advantage_player_1():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=1)

    assert game.score == "Advantage player 1"

def test_advantage_player_2():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)

    assert game.score == "Advantage player 2"

def test_back_to_deuce():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=1)

    assert game.score == "deuce"

def test_win_from_advantage():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)

    assert game.score == "Player 2 wins"


def test_win_player1_from_advantage():
    game = Game()
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=1)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=2)
    game.ball_result(player=1)
    game.ball_result(player=1)

    assert game.score == "Player 1 wins"
