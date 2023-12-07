from src.tennis_game.tennis import Game

def test_score_system():
    game = Game()
    possible_score = ["love", "15", "30", "40"]
    assert game.player1_score in possible_score
    assert game.player2_score in possible_score