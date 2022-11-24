import io
from contextlib import redirect_stdout

DIRECTORY = "golden_masters"

if __name__ == '__main__':

    # How to redirect stdout?
    f = io.StringIO()
    with redirect_stdout(f):
        print("Here is a console log which is redirected")
    redirected_stdout = f.getvalue()

    # How to write a file?
    with open("test.txt", "w") as e:
        e.write(redirected_stdout)
