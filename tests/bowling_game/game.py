from src.bowling_game.game import Game


def test_all_gutters_should_score_zero():
    game = Game()

    for i in range(0, 21):
        game.roll(0)
    final_score = game.score()

    assert final_score == 0


def test_basic_game_should_add_up_pins():
    game = Game()
    for i in range(1, 21):
        game.roll(1)
    final_score = game.score()

    assert final_score == 20


def test_spare_should_add_the_next_roll_as_bonus():
    game2 = Game()
    game2.roll(3)
    game2.roll(7) # 10 + next roll (1) --> 11

    for i in range(3, 21):
        game2.roll(1)
    final_score = game2.score()

    assert final_score == 29
