from src.data_munging.data_football import retrieve_csv

PATH = "tests/data_munging/football.csv"

def test_read_csv():

    assert retrieve_csv(PATH)