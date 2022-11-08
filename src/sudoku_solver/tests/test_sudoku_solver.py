import pytest
from src.sudoku_solver.sudoku_solver import solve, Grid, NoSolution


def test_solved_grid() -> None:
    input_grid: Grid = [
        [3, 9, 1, 2, 8, 6, 5, 7, 4],
        [4, 8, 7, 3, 5, 9, 1, 2, 6],
        [6, 5, 2, 7, 1, 4, 8, 3, 9],
        [8, 7, 5, 4, 3, 1, 6, 9, 2],
        [2, 1, 3, 9, 6, 7, 4, 8, 5],
        [9, 6, 4, 5, 2, 8, 7, 1, 3],
        [1, 4, 9, 6, 7, 3, 2, 5, 8],
        [5, 3, 8, 1, 4, 2, 9, 6, 7],
        [7, 2, 6, 8, 9, 5, 3, 4, 1],
    ]
    expected = input_grid
    solve(input_grid)
    assert input_grid == expected


def test_one_blank_cell() -> None:
    input_grid: Grid = [
        [3, 9, 1, 2, 8, 6, 5, 7, 4],
        [4, 8, 7, 3, 5, 9, 1, 2, 6],
        [6, 5, 2, 7, 1, 4, 8, 3, 9],
        [8, 7, 5, 4, 3, 1, 6, 9, 2],
        [2, 1, 3, 9, 6, 7, 4, 8, 5],
        [9, 6, 4, 5, 2, 8, 7, 1, 3],
        [1, 4, 9, 6, 7, 3, 2, 5, 8],
        [5, 3, 8, 1, 4, 2, 9, 6, 7],
        [7, 2, 6, 8, 9, 5, 3, 4, None],
    ]
    expected: Grid = [
        [3, 9, 1, 2, 8, 6, 5, 7, 4],
        [4, 8, 7, 3, 5, 9, 1, 2, 6],
        [6, 5, 2, 7, 1, 4, 8, 3, 9],
        [8, 7, 5, 4, 3, 1, 6, 9, 2],
        [2, 1, 3, 9, 6, 7, 4, 8, 5],
        [9, 6, 4, 5, 2, 8, 7, 1, 3],
        [1, 4, 9, 6, 7, 3, 2, 5, 8],
        [5, 3, 8, 1, 4, 2, 9, 6, 7],
        [7, 2, 6, 8, 9, 5, 3, 4, 1],
    ]
    solve(input_grid)
    assert input_grid == expected


def test_blank_square() -> None:
    input_grid: Grid = [
        [3, 9, 1, 2, 8, 6, 5, 7, 4],
        [4, 8, 7, 3, 5, 9, 1, 2, 6],
        [6, 5, 2, 7, 1, 4, 8, 3, 9],
        [8, 7, 5, 4, 3, 1, 6, 9, 2],
        [2, 1, 3, 9, 6, 7, 4, 8, 5],
        [9, 6, 4, 5, 2, 8, 7, 1, 3],
        [1, 4, 9, 6, 7, 3, None, None, None],
        [5, 3, 8, 1, 4, 2, None, None, None],
        [7, 2, 6, 8, 9, 5, None, None, None],
    ]
    expected: Grid = [
        [3, 9, 1, 2, 8, 6, 5, 7, 4],
        [4, 8, 7, 3, 5, 9, 1, 2, 6],
        [6, 5, 2, 7, 1, 4, 8, 3, 9],
        [8, 7, 5, 4, 3, 1, 6, 9, 2],
        [2, 1, 3, 9, 6, 7, 4, 8, 5],
        [9, 6, 4, 5, 2, 8, 7, 1, 3],
        [1, 4, 9, 6, 7, 3, 2, 5, 8],
        [5, 3, 8, 1, 4, 2, 9, 6, 7],
        [7, 2, 6, 8, 9, 5, 3, 4, 1],
    ]
    solve(input_grid)
    assert input_grid == expected


def test_not_possible() -> None:
    input_grid: Grid = [
        [None, 1, 2, 9, None, None, None, None, None],
        [3, 4, 5, None, None, None, None, None, None],
        [6, 7, 8, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]

    with pytest.raises(NoSolution):
        solve(input_grid)


def test_blank_grid() -> None:
    input_grid: Grid = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]
    solve(input_grid)
    print(input_grid)


def test_one_filled_in_cell() -> None:
    input_grid: Grid = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, 1],
    ]
    solve(input_grid)
    print(input_grid)
