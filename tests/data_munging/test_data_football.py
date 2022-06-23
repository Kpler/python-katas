from src.data_munging.data_football import retrieve_csv, get_min_goal_difference

PATH = "tests/data_munging/football.csv"

def test_read_csv():
    data = retrieve_csv(PATH)
    assert len(data) == 20

def test_get_min_goal_difference():
    data = retrieve_csv(PATH)
    assert get_min_goal_difference(data) == "Aston_Villa"