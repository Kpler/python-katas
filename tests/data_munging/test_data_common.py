import pytest

from src.data_munging.data_common import get_min_delta, parse_row, retrieve_csv

WEATHER_PATH = "tests/data_munging/weather.csv"
FOOTBALL_PATH = "tests/data_munging/football.csv"


def test_retrieve_weather_csv():
    data = retrieve_csv(WEATHER_PATH, 0, 0, 0)
    assert len(data) == 30


def test_retrieve_weather_csv_wrong_file():
    with pytest.raises(FileNotFoundError):
        retrieve_csv("team2", 0, 0, 0)


def test_find_minimum_weather_spread():
    data = retrieve_csv(WEATHER_PATH, 0, 1, 2)
    date_with_minimum_spread = get_min_delta(data)
    assert date_with_minimum_spread == '14'


def test_get_min_goal_difference():
    data = retrieve_csv(FOOTBALL_PATH, 1, 6, 7)
    assert get_min_delta(data) == "Aston_Villa"
