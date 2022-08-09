from src.bowling_game.game import Game


def test_all_gutters_should_score_zero():
    game = Game()

    for i in range(0, 21):
        game.roll(0)
    final_score = game.score()

    assert final_score == 0


def test_basic_game_should_add_up_pins():
    game = Game()

    print("Start score: " + str(game.current_score))

    for i in range(0, 21):
        game.roll(1)
        print(f"Current score: {game.current_score}")
    final_score = game.score()

    assert final_score == 20
