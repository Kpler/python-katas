from src.minesweeper.minesweeper import Minesweeper


def test_minesweeper_display() -> None:
    minesweeper = Minesweeper(4, 4, [])
    assert minesweeper.display() == "0000\n0000\n0000\n0000"

def test_bomb_insert() -> None:
    minesweeper = Minesweeper(4, 4, [(0,0)])
    assert minesweeper.display() == "*100\n1100\n0000\n0000" 

def test_bomb_insert_1() -> None:
    minesweeper = Minesweeper(4, 4, [(3,3)])
    assert minesweeper.display() == "0000\n0000\n0011\n001*"

def test_bomb_insert_2() -> None:
    minesweeper = Minesweeper(4, 4, [(3,3),(2,2)])
    assert minesweeper.display() == "0000\n0111\n01*2\n012*"