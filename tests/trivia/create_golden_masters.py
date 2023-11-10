import io
import sys
sys.path.append("/home/lenovokpler/kpler/kata/python-katas")
from contextlib import redirect_stdout
from src.trivia.trivia import main


DIRECTORY = "golden_masters"

if __name__ == '__main__':

    inputs_to_files = [
        ([1, ["Chet", "Pat", "Sue"]], "test_1"),
        ([3, ["Chet", "Pat", "Sue"]], "test_2")
    ]

    for inputs, file in inputs_to_files:
        # How to redirect stdout?
        f = io.StringIO()
        with redirect_stdout(f):
            main(*inputs)
        redirected_stdout = f.getvalue()

        # How to write a file?
        with open(f"{DIRECTORY}/{file}.txt", "w") as e:
            e.write(redirected_stdout)
