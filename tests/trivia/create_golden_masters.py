import io
from contextlib import redirect_stdout
from trivia.trivia import main

DIRECTORY = "golden_masters"

if __name__ == '__main__':

    # How to redirect stdout?
    f = io.StringIO()
    with redirect_stdout(f):
        main(1, ["Chet", "Pat", "Sue"])
    redirected_stdout = f.getvalue()

    # How to write a file?
    with open("test.txt", "w") as e:
        e.write(redirected_stdout)
