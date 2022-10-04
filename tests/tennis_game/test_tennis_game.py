from src.tennis_game.tennis_game import Tennis


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score == "0"
  