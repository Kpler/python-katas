from typing import Optional

Grid = list[list[Optional[int]]]


class NoSolution(Exception):
    pass


def find_row_values(grid: Grid, row_index: int) -> set[int]:
    return set([value for value in grid[row_index] if value is not None])


def find_column_values(grid: Grid, column_index: int) -> set[int]:
    return set([value for row in grid if (value := row[column_index]) is not None])


def find_square_values(grid: Grid, row_index: int, column_index: int) -> set[int]:
    square_row_index_start = row_index - (row_index % 3)
    square_column_index_start = column_index - (column_index % 3)

    output: set[int] = set()
    for i in range(square_row_index_start, square_row_index_start + 3):
        for j in range(square_column_index_start, square_column_index_start + 3):
            value = grid[i][j]
            if value is not None:
                output.add(value)
    return output


def find_possible_values(grid: Grid, row_index: int, column_index: int) -> list[int]:
    possiblities = set(range(1, 10))
    row_values = find_row_values(grid, row_index)
    column_values = find_column_values(grid, column_index)
    square_values = find_square_values(grid, row_index, column_index)
    possible_values = possiblities - row_values - column_values - square_values
    return list(possible_values)


def solve(input_grid: Grid) -> None:
    for row_index, row in enumerate(input_grid):
        for cell_index, cell in enumerate(row):
            if cell != None:
                continue

            possible_values = find_possible_values(input_grid, row_index, cell_index)
            if len(possible_values) == 0:
                raise NoSolution()

            index = 0
            solution_found = False
            while not solution_found:
                input_grid[row_index][cell_index] = possible_values[index]
                try:
                    solve(input_grid)
                except NoSolution:
                    if index + 2 > len(possible_values):
                        input_grid[row_index][cell_index] = None
                        raise NoSolution()
                    index += 1
                else:
                    solution_found = True
