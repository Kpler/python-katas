from src.tennis_game.tennis import Game


def test_create_game_starts_at_love_love():
    game = Game()
    assert not game.is_finished()
    assert game.get_score() == "love-love"


def test_update_player_score():
    game = Game()
    game.player_1_scored()
    assert not game.is_finished()
    assert game.get_score() == "15-love"
