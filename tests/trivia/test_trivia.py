import pytest as pytest

from src.trivia.trivia import main
import io
from contextlib import redirect_stdout

DIRECTORY = "golden_masters"
seeds = [237, 345, 42]

if __name__ == '__main__':
    f = io.StringIO()
    for seed in seeds:
        with open(f"{DIRECTORY}/seed_{seed}.txt", "r") as e:
            fff = e.read()

        with redirect_stdout(f):
            main(seed)
        out = f.getvalue()


@pytest.mark.parametrize("seed", seeds)
def test_trivia_seeds(seed):
    f = io.StringIO()
    with redirect_stdout(f):
        main(seed)
    result = f.getvalue()

    with open(f"{DIRECTORY}/seed_{seed}.txt", "r") as file:
        expected = file.read()

    assert result == expected

