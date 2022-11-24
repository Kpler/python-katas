# Trivia

This code is a legacy code taken from [here](https://github.com/jbrains/trivia), on which we can perform various Katas.

## Golden Master testing

What is the Golden Master Technique? Check [here](https://docs.google.com/presentation/d/1Vxj24fppuC4Sd13yLKCg7RQrUkuRuyGuF6N2yXEGtQM/edit#slide=id.g191f97a467f_0_3)

Goal:
    1. Write a program to generate golden masters (complete the file xxx)
    2. Write a test suite to assert that the golden masters's inputs always gives the golden master's output
    3. Check coverage
    4. Introduce breaking change

Tips:
	capture stdout
	random.seed

add pytest-cov
pytest --cov=../../src/trivia

TODO: prepare a clean branch, extract the Game from main?