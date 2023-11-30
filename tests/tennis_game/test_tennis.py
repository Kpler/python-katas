from src.tennis_game.game import Game


def test_if_score_in_allowed_values():
    game = Game()
    score_1 = game.get_score(game.player1)
    score_2 = game.get_score(game.player2)
    allowed_scores = ["love", "15", "30", "40", "adv"]
    assert score_1 in allowed_scores
    assert score_2 in allowed_scores

def test_if_winning():
    game = Game()
    game.player1.points = 3
    game.player2.points = 1

    game.player1.points += 1

    assert game.get_winner() == game.player1.name

def test_if_deuce():
    game = Game()
    game.player1.points = 4
    game.player2.points = 4
    assert game.get_winner() is None


def test_difference_less_than_one():
    game = Game()
    game.player1.points = 5
    game.player2.points = 4
    assert game.get_winner() is None


def test_points_more_than_four():
    game = Game()
    game.player1.points = 5
    game.player2.points = 5
    assert game.get_winner() is None


def test_add_score():
    game = Game()
    game.add_points(game.player1)
    game.add_points(game.player1)
    assert game.player1.points == 2


def test_scores_below_four():
    game = Game()
    game.player1.points = 2
    game.player2.points = 1
    assert game.print_score() == "30:15"


def test_single_player_scores_above_four():
    game = Game()
    game.player1.points = 5
    game.player2.points = 4
    assert game.print_score() == "player1 adv"

