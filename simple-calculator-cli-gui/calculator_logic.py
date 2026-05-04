# calculator_logic.py
# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division with zero check
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
