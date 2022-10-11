
def compute_neighbor_count(grid: list[list[int]], row_index: int, cell_index: int) -> int:
    count = 0
    for neighbor_row_index in range(row_index-1, row_index+2):
        for neighbor_cell_index in range(cell_index-1, cell_index+2):
            is_itself = neighbor_row_index == row_index and neighbor_cell_index == cell_index
            if not is_itself and grid[neighbor_row_index][neighbor_cell_index] == 1:
                count += 1
    return count

def compute_cell_state(grid: list[list[int]], row_index: int, cell_index: int) -> int:
    cell = grid[row_index][cell_index]
    if cell == 1:
        neighbor_count = compute_neighbor_count(grid, row_index, cell_index)
        if neighbor_count < 2 or neighbor_count > 3:
            return 0
        else:
            return 1
    else:
        return 0

def compute_next_state(grid: list[list[int]]) -> list[list[int]]:
    output_grid: list[list[int]] = []

    for row_index, row in enumerate(grid):
        output_row: list[int] = []
        for cell_index, cell in enumerate(row):
            new_cell = compute_cell_state(grid, row_index, cell_index)
            output_row.append(new_cell)
        output_grid.append(output_row)
    return output_grid