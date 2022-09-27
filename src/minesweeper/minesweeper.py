class GameOver(Exception):
    pass


class WinningGame(Exception):
    pass


class Minesweeper:
    def __init__(self, rows: int, columns: int, bombs: list[tuple[int, int]]) -> None:
        self._rows = rows
        self._columns = columns
        self._bombs = bombs
        self._grid = self._build_grid("0")
        self._set_bombs()
        self._moves_grid = self._build_grid(".")

    # This is a method (not a function) because it's within a class
    def _build_grid(self, char: str) -> list[list[str]]:
        grid = []
        for i in range(self._rows):
            inner_grid = []
            for j in range(self._columns):
                inner_grid.append(char)
            grid.append(inner_grid)
        return grid

    def _set_bombs(self) -> None:
        for (row, column) in self._bombs:
            self._grid[row][column] = "*"
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if (
                        i > self._rows - 1
                        or i < 0
                        or j > self._columns - 1
                        or j < 0
                        or self._grid[i][j] == "*"
                    ):
                        continue
                    temp_int = int(self._grid[i][j])
                    temp_int += 1
                    self._grid[i][j] = str(temp_int)

    def _print(self, grid: list[list[str]]) -> str:
        return "\n".join(["".join(row) for row in grid])

    def display(self) -> str:
        return self._print(self._grid)

    def play(self, row: int, column: int) -> str:
        self._moves_grid[row][column] = self._grid[row][column]

        if self._grid[row][column] == "*":
            raise GameOver()

        if self._grid[row][column] == "0":
            for r in range(row-1,row+2):
                for c in range(column-1,column+2):
                    if (
                        r > self._rows - 1
                        or r < 0
                        or c > self._columns - 1
                        or c < 0
                        or self._moves_grid[r][c] != "."
                    ):
                        continue
                    self.play(r,c)

        count_unswept = 0
        for moves_row in self._moves_grid:
            for moves_cell in moves_row:
                if moves_cell == ".":
                    count_unswept += 1
        if count_unswept == len(self._bombs):
            raise WinningGame()

        return self._print(self._moves_grid)
