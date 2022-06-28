from src.data_munging.data_common import retrieve_csv


def test_retrieve_csv():
    lines = retrieve_csv(path)
    assert len(lines) == 20