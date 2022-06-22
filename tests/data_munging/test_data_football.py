import pytest

from src.data_munging.data_football import retrieve_csv, compute_difference


PATH = "tests/data_munging/football.csv"


def test_read_csv():
    data = retrieve_csv(PATH)
    assert len(data) == 20


def test_read_csv_wrong_file():
    with pytest.raises(FileNotFoundError):
        retrieve_csv("team2")


def test_should_compute_difference():
    input_row = ["1", "Arsenal", "38", "26", "9", "3", "79", "36", "87", ""]
    assert compute_difference(input_row) == ("Arsenal", 43)

def test_should_compute_smallest_difference():
    assert compute_smallest_difference() == 4
