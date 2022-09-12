class Minesweeper:
    def __init__(self, rows: int, columns: int, bombs: list[tuple[int, int]]) -> None:
        self.rows = rows
        self.columns = columns
        self.bombs = bombs

    def display(self) -> str:
        grid = []
        for i in range(self.rows):
            inner_grid = []
            for j in range(self.columns):
                inner_grid.append(".")
            grid.append(inner_grid)

        for (row,column) in self.bombs:
            grid[row][column] = "*"

        return "\n".join(["".join(row) for row in grid])
