from src.tennis_game.tennis import Game

possible_score = ["love", "15", "30", "40"]

def test_score_system():
    game = Game()
    assert game.player1_score in possible_score
    assert game.player2_score in possible_score

def test_score_format():
    game = Game()
    game.player1_score = "love"
    assert game.player1_score in possible_score
    game.player1_score = "15"
    assert game.player1_score in possible_score
    game.player1_score = "30"
    assert game.player1_score in possible_score
    game.player1_score = "40"
    assert game.player1_score in possible_score

def test_win_game_player1():
    game = Game()
    game.player1_points = 3
    game.player1_score = "40"
    game.player1_points += 1
    assert game.get_winner() == "player1"

def test_win_game_player2():
    game = Game()
    game.player2_points = 3
    game.player2_score = "40"
    game.player2_points += 1
    assert game.get_winner() == "player2"

def test_deuce():
    game = Game()
    game.player1_points = 3
    game.player2_points = 3
    game.player1_score = "40"
    game.player2_score = "40"
    assert game.get_score() == "deuce"


def test_score_display():
    game = Game()
    game.play_one_ball()
    assert game.get_score() in ["love-15", "15-love"]

