from src.tennis_game.game import Game

def test_when_game_start_then_score_is_0_0():
    g = Game()
    g.start()
    assert g.score == "love-love"

def test_number_of_players_equal_2():
    g = Game()
    g.start()
    assert g.nb_players == 2

def test_when_first_player_scores_should_be_15_love():
    g = Game()
    g.start()
    g.player_1_scores()
    assert g.score == "15-love"

def test_when_second_player_scores_should_be_love_15():
    g = Game()
    g.start()
    g.player_2_scores()
    assert g.score == "love-15"

def test_when_second_player_scores_twice_should_be_love_30():
    g = Game()
    g.start()
    g.player_2_scores()
    g.player_2_scores()
    assert g.score == "love-30"
