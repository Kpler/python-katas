from src.trivia.trivia import main
import io
from contextlib import redirect_stdout


if __name__ == '__main__':
    f = io.StringIO()
    with redirect_stdout(f):
        main(237)
    out = f.getvalue()

