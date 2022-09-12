from src.minesweeper.minesweeper import Minesweeper


def test_minesweeper_display() -> None:
    minesweeper = Minesweeper(4, 4, [])
    assert minesweeper.display() == "....\n....\n....\n...."
