# Trivia

This code is a legacy code taken from [here](https://github.com/jbrains/trivia), on which we can perform various Katas.

## Golden Master testing

What is the Golden Master Technique? Check [here](https://docs.google.com/presentation/d/1Vxj24fppuC4Sd13yLKCg7RQrUkuRuyGuF6N2yXEGtQM/edit#slide=id.g191f97a467f_0_3)

The goal of this Kata is the following:
    1. Complete `tests/trivia/create_golden_master.py` in order to generate golden masters files
    2. Complete `tests/trivia/test_trivia.py` to have a test suite to assert that the golden masters's inputs always gives the golden master's output
    3. Check the coverage with `pytest --cov=$COVERED_FOLDER $TESTS_FOLDER`
    4. Be confident to refactor
