import hashlib
import pytest
import sys

from src.trivia.trivia import main

@pytest.mark.run_these_please
def test_trivia():

    with open("current_test_output.txt", "w") as e:
        sys.stdout = e
        for i in range(1, 10):
            main(i, ["Chet", "Pat", "Sue"])

    golden_hash = hashlib.md5(open('golden_master.txt', 'rb').read()).hexdigest()
    current_output_hash = hashlib.md5(open('current_test_output.txt', 'rb').read()).hexdigest()

    assert golden_hash == current_output_hash
