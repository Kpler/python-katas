def calculate(expression: str) -> float:

    try:
        result = eval(expression)
    except (SyntaxError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {expression}. Error: {e}")
    
    return result

try:
    result = calculate("5 + 3 * 2")
    print("Result:", result)
except ValueError as e:
    print("Error:", e)