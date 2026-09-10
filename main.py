# Import the reusable calculator_tools package.
import calculator_tools

# Import the custom exception for handling unsupported operations.
from calculator_tools import InvalidOperationError


# Define the main function that demonstrates the package.
def main():
    """Demonstrate package functionality and error handling."""
    # Demonstrate addition.
    print("Addition:", calculator_tools.add(10, 5))
    # Demonstrate subtraction.
    print("Subtraction:", calculator_tools.subtract(10, 5))
    # Demonstrate multiplication.
    print("Multiplication:", calculator_tools.multiply(10, 5))
    # Demonstrate division.
    print("Division:", calculator_tools.divide(10, 5))
    # Demonstrate percentage calculation.
    print("20% of 500:", calculator_tools.percentage(500, 20))
    # Demonstrate average calculation.
    print("Average:", calculator_tools.average([10, 20, 30, 40]))
    # Demonstrate Celsius-to-Fahrenheit conversion.
    print("25 C in Fahrenheit:", calculator_tools.celsius_to_fahrenheit(25))
    # Demonstrate Fahrenheit-to-Celsius conversion.
    print("77 F in Celsius:", calculator_tools.fahrenheit_to_celsius(77))
    # Demonstrate meters-to-kilometers conversion.
    print("5000 m in km:", calculator_tools.convert_units(5000, "m", "km"))

    # Try an operation that causes division by zero.
    try:
        # Pass zero as the divisor to test exception handling.
        calculator_tools.divide(10, 0)
    except ZeroDivisionError as error:
        # Catch the error and print a clear message.
        print("Handled division error:", error)

    # Try an operation with an incorrect data type.
    try:
        # Pass a string where a number is expected.
        calculator_tools.add("10", 5)
    except TypeError as error:
        # Catch the type error and print a clear message.
        print("Handled type error:", error)

    # Try an invalid percentage.
    try:
        # Pass a negative percentage to test value validation.
        calculator_tools.percentage(500, -10)
    except ValueError as error:
        # Catch the value error and print a clear message.
        print("Handled value error:", error)

    # Try an unsupported arithmetic operation.
    try:
        # Use the module's calculate() function with an unsupported name.
        calculator_tools.arithmetic.calculate("power", 2, 3)
    except InvalidOperationError as error:
        # Catch the custom exception and print a clear message.
        print("Handled custom operation error:", error)

    # Try an unsupported unit conversion.
    try:
        # Request conversion to a unit that is not supported.
        calculator_tools.convert_units(10, "m", "yard")
    except InvalidOperationError as error:
        # Catch the custom exception and print a clear message.
        print("Handled custom conversion error:", error)


# Check whether this file is being run directly.
if __name__ == "__main__":
    # Call main() to start the demonstration.
    main()
