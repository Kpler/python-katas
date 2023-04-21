# Calculator Kata

Imagine you are about to write a software like [Wolfram Alpha](https://www.wolframalpha.com/) 
or @AlexG favorite [Numi](https://numi.app/). 
You are tasked to create a function that takes a computation string as input and returns the result.


## Instructions

Implement `calculate` function that accepts the input and returns float result.
```python
def calculate(expression: str) -> float:
    # TODO: Implement calculator logic here
    return 0
```

- All **numbers** and operators in the input are **surrounded** by a **single space** for convenient parsing.
- For simplicity the **inputs** are only **integers** (negative and positive whole numbers).

### Level 1: Addition and Subtraction
Implement `+` and `-` operators.
```yaml
1 + 2 # Result: 3
5 - 3 # Result: 2
10 + 20 - 5 # Result: 25
100 - 50 + 25 # Result: 75
4 + 8 + 15 + 16 + 23 + 42 # Result: 108
```


### Level 2: Implement Multiplication
Implement `*` operator and deal correctly with the order of operations.
```yaml
2 * 3 # Result: 6
2 * 5 * 10 # Result: 100
2 + 3 * 4 # Result: 14
2 * 3 + 4 # Result: 10
3 * 4 + 5 * 6 # Result: 42
```


### (Optional) Level 3: Add Parenthesis
Implement handling of `()`.
```yaml
80 + (20 - 5) # Result: 95
5 - ( 3 + 2 ) + 1 # Result: 1
3 * ( 5 + 3 ) # Result: 24
( 1 + 2 ) * 3 # Result: 9
( 1 + 2 ) * ( 3 + 4 ) - 1 # Result: 20
```
