from src.tennis_game.tennis_game import Player


def test_player_status():
    player = Player()
    assert player.get_status() == "love"
    player.increase_score()
    assert player.get_status() == "15"
    player.increase_score()
    assert player.get_status() == "30"
    player.increase_score()
    assert player.get_status() == "40"

def test_is_deuce():
    pass
