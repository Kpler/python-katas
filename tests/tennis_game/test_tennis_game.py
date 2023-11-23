
def test_assure_scores():
    allowed_states = ["L", "15", "30", "40", "A"]
    assert match.player1_score in allowed_states
    assert match.player2_score in allowed_states