def test_player_status():
    player = Player()
    assert player.status == 'love'
    player.increase_score()
    assert player.status == '15'
    player.increase_score()
    assert player.status == '30'
    player.increase_score()
    assert player.status == '40'