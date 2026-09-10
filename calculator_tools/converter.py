# Import the custom exception for unsupported units.
from .exceptions import InvalidOperationError


# Define a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # Validate the temperature type.
    if not isinstance(celsius, (int, float)):
        # Raise TypeError when the temperature is not numeric.
        raise TypeError("Temperature must be numeric.")
    # Apply the Celsius-to-Fahrenheit formula.
    return (celsius * 9 / 5) + 32


# Define a function to convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # Validate the temperature type.
    if not isinstance(fahrenheit, (int, float)):
        # Raise TypeError when the temperature is not numeric.
        raise TypeError("Temperature must be numeric.")
    # Apply the Fahrenheit-to-Celsius formula.
    return (fahrenheit - 32) * 5 / 9


# Define a function for simple length conversion.
def convert_units(value, from_unit, to_unit):
    """Convert between supported length units."""
    # Validate the numeric value.
    if not isinstance(value, (int, float)):
        # Raise TypeError when the value is not numeric.
        raise TypeError("Conversion value must be numeric.")
    # Validate the source unit type.
    if not isinstance(from_unit, str):
        # Raise TypeError when the source unit is not a string.
        raise TypeError("from_unit must be a string.")
    # Validate the destination unit type.
    if not isinstance(to_unit, str):
        # Raise TypeError when the destination unit is not a string.
        raise TypeError("to_unit must be a string.")
    # Normalize both unit names to lowercase.
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    # Store conversion factors relative to one meter.
    factors = {
        "m": 1, "meter": 1, "meters": 1,
        "km": 1000, "kilometer": 1000, "kilometers": 1000,
        "cm": 0.01, "centimeter": 0.01, "centimeters": 0.01,
        "mi": 1609.344, "mile": 1609.344, "miles": 1609.344
    }
    # Check whether the source unit is supported.
    if from_unit not in factors:
        # Raise the custom exception for an unsupported source unit.
        raise InvalidOperationError(f"Unsupported source unit: {from_unit}")
    # Check whether the destination unit is supported.
    if to_unit not in factors:
        # Raise the custom exception for an unsupported destination unit.
        raise InvalidOperationError(f"Unsupported destination unit: {to_unit}")
    # Convert the input value to meters.
    meters = value * factors[from_unit]
    # Convert meters to the requested destination unit.
    return meters / factors[to_unit]
