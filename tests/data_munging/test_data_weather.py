import pytest
from src.data_munging.data_weather import find_minimum_spread_date, retrieve_csv


PATH = "tests/data_munging/weather.csv"


def test_read_csv():
    data = retrieve_csv(PATH)
    assert len(data) == 30


def test_read_csv_wrong_file():
    with pytest.raises(FileNotFoundError):
        retrieve_csv("team2")


def test_find_minimum_spread():
    data = retrieve_csv(PATH)
    date_with_minimum_spread = find_minimum_spread_date(data)
    assert date_with_minimum_spread == 14
