from zombie_survival.game import ZombieSurvivalGame, Survivor


def test_initialize_game():
    game = ZombieSurvivalGame()
    assert game is not None
    assert game.survivors is not None
    assert len(game.survivors) >= 1

def test_init_survivor() -> None:
    survivor = Survivor("nicolas")
    assert survivor.health == 100
    assert survivor.energy == 100
    assert survivor.zombie_killed == 0
    assert survivor.is_alive is True

def test_fight() -> None:
    survivor = Survivor("nicolas")
    survivor.fight()
    assert survivor.energy == 70
    assert survivor.zombie_killed == 1
    assert survivor.health == 90

def test_fight_twice() -> None:
    survivor = Survivor("nicolas")
    survivor.fight()
    survivor.fight()
    assert survivor.energy == 40
    assert survivor.zombie_killed == 2
    assert survivor.health == 80

def test_fight_with_few_energy() -> None:
    survivor = Survivor("nicolas")
    survivor.energy = 20
    survivor.fight()
    assert survivor.energy == 20
    assert survivor.health == 80
    assert survivor.is_alive == True
    assert survivor.zombie_killed == 0


def test_rest_restore_40_energy() -> None:
    survivor = Survivor("fabien")
    survivor.energy = 50
    survivor.rest()
    assert survivor.energy == 90

def test_rest_restore_100_energy() -> None:
    survivor = Survivor("fabien")
    survivor.energy = 80
    survivor.rest()
    assert survivor.energy == 100

def test_rest_dead_survivor_does_not_rest()->None:
    survivor = Survivor("henry")
    survivor.is_alive = False
    survivor.energy = 20
    survivor.rest()
    assert survivor.energy == 20

def test_survivor_fights_and_die()->None:
    survivor = Survivor("henry")
    survivor.energy = 20
    survivor.health = 15
    survivor.fight()
    assert not survivor.is_alive
    assert survivor.health == 0

def test_survivor_heals()->None:
    survivor = Survivor("henry")
    survivor.energy = 30
    survivor.health = 15
    survivor.heal()
    assert survivor.energy == 10
    assert survivor.health == 40

def test_survivor_heal_without_enough_energy()->None:
    survivor = Survivor("virginie")
    survivor.energy = 10
    survivor.health = 15
    survivor.heal()
    assert survivor.energy == 10
    assert survivor.health == 15

def test_run_away_ends_the_game()->None:
    game = ZombieSurvivalGame()
    survivor = game.survivors[0]
    survivor.run_away()
    assert survivor.is_alive is True
    assert game.game_over is True

def test_fight_with_game_over()->None:
    game = ZombieSurvivalGame()
    game.game_over = True
    survivor1 = game.survivors[0]
    survivor1.fight()
    assert survivor1.energy == 100
    assert survivor1.health == 100