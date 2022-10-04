from src.tennis_game.tennis_game import Tennis


def test_initial_score_should_be_zero():
  game = Tennis()
  score = game.get_game_score()
  assert score == "0-0"

def test_first_score_should_be_incremeted():
  game = Tennis()
  game.play("0")
  score = game.get_game_score()
  assert score == "15-0"

def test_score_should_be_incremeted_all_points():
  game = Tennis()
  game.play("0")
  game.play("1")
  game.play("0")
  game.play("1")
  game.play("0")
  game.play("1")
  score = game.get_game_score()
  assert score == "40-40"
