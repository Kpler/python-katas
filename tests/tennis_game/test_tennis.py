from src.tennis_game.tennis import Game

possible_score = ["love", "15", "30", "40"]

def test_score_system():
    game = Game()
    assert game.player1_score in possible_score
    assert game.player2_score in possible_score

def test_score_format():
    game = Game()
    game.player1_point = 1
    assert game.player1_score == "15"