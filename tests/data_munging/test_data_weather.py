import pytest
from src.data_munging.data_weather import retrieve_csv


PATH = './tests/data_munging/weather.csv'

def test_read_csv():
    data = retrieve_csv(PATH)
    assert data is not None
