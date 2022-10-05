from src.tennis_game.tennis import Game


def test_create_game_starts_at_love_love():
    game = Game()
    assert not game.is_finished()
    assert game.get_score() == "love-love"


def test_player_1_scored():
    game = Game()
    game.player_1_scored()
    assert not game.is_finished()
    assert game.get_score() == "15-love"


def test_player_1_win_the_game_without_deuce():
    game = Game()
    game.player_1_scored()
    game.player_1_scored()
    game.player_1_scored()
    game.player_1_scored()
    assert game.is_finished()
    assert game.get_score() == "Player 1 wins"

def test_player_2_win_the_game_without_deuce():
    game = Game()
    game.player_2_scored()
    game.player_2_scored()
    game.player_2_scored()
    game.player_2_scored()
    assert game.is_finished()
    assert game.get_score() == "Player 2 wins"
