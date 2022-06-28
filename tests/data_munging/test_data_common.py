from src.data_munging.data_common import get_min_spread, parse_row, retrieve_csv

PATH = "tests/data_munging/football.csv"


def test_retrieve_csv():
    lines = retrieve_csv(path=PATH)
    assert len(lines) == 20


def test_row_delta():
    row = "1,88,59,74,,53.8,,0.00,F,280,9.6,270,17,1.6,93,23,1004.5".split(",")
    res = parse_row(row, 0, 2, 1)
    assert res.delta == 29


def test_get_min_spread():
    data = retrieve_csv(PATH)
    assert get_min_spread(data) == "Aston_Villa"
