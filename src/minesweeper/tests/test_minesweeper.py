import pytest
from src.minesweeper.minesweeper import Minesweeper, GameOver, WinningGame


def test_minesweeper_display() -> None:
    minesweeper = Minesweeper(4, 4, [])
    assert minesweeper.display() == "0000\n0000\n0000\n0000"


def test_bomb_insert() -> None:
    minesweeper = Minesweeper(4, 4, [(0, 0)])
    assert minesweeper.display() == "*100\n1100\n0000\n0000"


def test_bomb_insert_1() -> None:
    minesweeper = Minesweeper(4, 4, [(3, 3)])
    assert minesweeper.display() == "0000\n0000\n0011\n001*"


def test_bomb_insert_2() -> None:
    minesweeper = Minesweeper(4, 4, [(3, 3), (2, 2)])
    assert minesweeper.display() == "0000\n0111\n01*2\n012*"


def test_play() -> None:
    minesweeper = Minesweeper(4, 4, [(0, 0), (1, 3)])
    assert minesweeper.play(0, 1) == ".1..\n....\n....\n...."
    assert minesweeper.play(0, 2) == ".11.\n....\n....\n...."


def test_game_over() -> None:
    minesweeper = Minesweeper(4, 4, [(0, 0)])
    with pytest.raises(GameOver):
        minesweeper.play(0, 0)


def test_win_game() -> None:
    minesweeper = Minesweeper(2, 2, [(0, 0)])
    minesweeper.play(0, 1)
    minesweeper.play(1, 0)
    with pytest.raises(WinningGame):
        minesweeper.play(1, 1)


def test_almost_win_game() -> None:
    minesweeper = Minesweeper(2, 2, [(0, 0)])
    minesweeper.play(0, 1)
    minesweeper.play(1, 0)
    with pytest.raises(GameOver):
        minesweeper.play(0, 0)


def test_reveal_adjacent_cells_when_a_zero_is_clicked() -> None:
    minesweeper = Minesweeper(4, 4, [(1, 1)])
    assert minesweeper.play(0, 3) == "..10\n..10\n1110\n0000"

    # ..10
    # ..10
    # 1110
    # 0000
