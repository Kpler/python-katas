from src.tennis_game.tennis import Game


def test_create_game_starts_at_love_love():
    game = Game()
    assert not game.is_finished()
    assert game.get_score() == 'love-love'

# def test_create_game_starts_at_love_love():
#     game = Game()
#     assert not game.is_finished()
#     assert game.get_score() == 'love-love'