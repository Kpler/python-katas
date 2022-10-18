from src.game_of_life.game_of_life import compute_next_state


def test_cells_stay_alive() -> None:
    input = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    expected = input

    output = compute_next_state(input)
    assert expected == output


def test_cells_die_if_not_enough_neighbors() -> None:
    input = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    output = compute_next_state(input)
    assert expected == output


def test_cells_die_if_too_many_neighbors() -> None:
    input = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    expected = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    output = compute_next_state(input)
    assert expected == output


def test_boundaries_handled_properly() -> None:
    input = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    expected = input

    output = compute_next_state(input)
    assert expected == output


def test_dead_cell_with_three_neighbors_is_born() -> None:
    input = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    expected = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]

    output = compute_next_state(input)
    assert expected == output
