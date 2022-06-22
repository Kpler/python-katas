import pytest

from src.data_munging.data_football import retrieve_csv


PATH = "tests/data_munging/football.csv"


def test_read_csv():
    data = retrieve_csv(PATH)
    assert len(data) == 20


def test_read_csv_wrong_file():
    with pytest.raises(FileNotFoundError):
        retrieve_csv("team2")
