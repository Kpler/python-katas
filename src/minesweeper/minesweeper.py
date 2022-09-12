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
                inner_grid.append("0")
            grid.append(inner_grid)

        for (row,column) in self.bombs:
            grid[row][column] = "*"
            for i in range(row-1,row+2):
                for j in range(column-1,column+2):
                    if i > self.rows-1 or i < 0 or j > self.columns-1 or j < 0 or grid[i][j] == "*":
                        continue
                    temp_int = int(grid[i][j])
                    temp_int += 1
                    grid[i][j] = str(temp_int)


        return "\n".join(["".join(row) for row in grid])
