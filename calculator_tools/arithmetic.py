# Import the custom exception from this package.
from .exceptions import InvalidOperationError


# Define a function for addition.
def add(a, b):
    """Return the sum of two numbers."""
    # Check that both inputs are numeric.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise TypeError when an input has an incorrect type.
        raise TypeError("add() requires numeric values.")
    # Return the addition result.
    return a + b


# Define a function for subtraction.
def subtract(a, b):
    """Return the difference between two numbers."""
    # Validate both inputs.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise TypeError for incorrect data types.
        raise TypeError("subtract() requires numeric values.")
    # Return the subtraction result.
    return a - b


# Define a function for multiplication.
def multiply(a, b):
    """Return the product of two numbers."""
    # Validate both inputs.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise TypeError for incorrect data types.
        raise TypeError("multiply() requires numeric values.")
    # Return the multiplication result.
    return a * b


# Define a function for division.
def divide(a, b):
    """Return the quotient of two numbers."""
    # Validate both inputs.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # Raise TypeError for incorrect data types.
        raise TypeError("divide() requires numeric values.")
    # Check the divisor before dividing.
    if b == 0:
        # Raise ZeroDivisionError instead of allowing an invalid calculation.
        raise ZeroDivisionError("Cannot divide by zero.")
    # Return the division result.
    return a / b


# Define a function for percentage calculation.
def percentage(value, percent):
    """Return the specified percentage of a value."""
    # Validate both numeric inputs.
    if not isinstance(value, (int, float)) or not isinstance(percent, (int, float)):
        # Raise TypeError for incorrect data types.
        raise TypeError("percentage() requires numeric values.")
    # Reject a negative percentage.
    if percent < 0:
        # Raise ValueError because a negative percentage is invalid here.
        raise ValueError("Percentage cannot be negative.")
    # Return the calculated percentage.
    return value * percent / 100


# Define a function that selects an arithmetic operation by name.
def calculate(operation, a, b):
    """Perform a supported arithmetic operation by name."""
    # Store operation names and their corresponding functions.
    operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    # Check whether the requested operation is supported.
    if operation not in operations:
        # Raise the custom exception for an unsupported operation.
        raise InvalidOperationError(f"Unsupported operation: {operation}")
    # Call the selected function and return its result.
    return operations[operation](a, b)
