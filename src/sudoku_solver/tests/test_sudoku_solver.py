import pytest
from src.sudoku_solver.sudoku_solver import solve, Grid

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
    output_grid = solve(input_grid)
    assert(output_grid == expected)


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
    output_grid = solve(input_grid)
    assert(output_grid == expected)