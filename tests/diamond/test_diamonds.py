from src.diamond.diamonds import build_diamond, get_iteration_count


def test_build_diamond_return_given_A():
    assert build_diamond('A') == 'A'


def test_build_diamond_return_given_B():
    assert build_diamond('B') == " A \nB B\n A "


def test_iteration_count_given_A():
    assert get_iteration_count("A") == 1
