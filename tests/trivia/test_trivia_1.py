import pytest as pytest
import io
from contextlib import redirect_stdout
from src.trivia.trivia import main
from tests.trivia.create_golden_masters import DIRECTORY

an_example_to_use_parametrize = [
    ("test_1.txt", [1, ["Chet", "Pat", "Sue"]]),
    ("test_2.txt", [3, ["Chet", "Pat", "Sue"]]),
]


@pytest.mark.parametrize("file_name, inputs", an_example_to_use_parametrize)
def test_trivia_first_run(file_name, inputs):
    assert file_name == file_name

    f = io.StringIO()
    with redirect_stdout(f):
        main(*inputs)
    redirected_stdout = f.getvalue()

    with open(f"{DIRECTORY}/{file_name}", "r") as e:
        file_name_stdout = e.read()

    assert redirected_stdout == file_name_stdout

