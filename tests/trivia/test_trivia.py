from src.trivia.trivia import main
import io
from contextlib import redirect_stdout

DIRECTORY = "golden_masters"

if __name__ == '__main__':
    f = io.StringIO()
    seeds = [237, 345, 42]
    
    for seed in seeds:
        with open(f"{DIRECTORY}/seed_{seed}.txt", "r") as e:
            fff = e.read()

        with redirect_stdout(f):
            main(seed)
        out = f.getvalue()


