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

def test_win_without_deuce():
    game = Game()
    game.p1.increase_score()
    game.p1.increase_score()
    game.p1.increase_score()
    game.p1.increase_score()
    assert game.status == 'over'
    assert game.winner == game.p1
    assert game.score == [40, 0]
