import pytest

class Tennis:

  current_player: str

  game_score: {
    one: int,
    two: int,
  }

  # win 6 games/sets to win match; need 2 difference

  # match_score: []
 
  play(winner: str):


  get_score():
    return score


def test_initial_score_should_be_zero:
  game = new Tennis()
  assert game.get_score() == { one: 0, two: 0 }
  

