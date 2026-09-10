# Define a function for calculating an average.
def average(values):
    """Return the average of a non-empty list or tuple of numbers."""
    # Check that the input is a list or tuple.
    if not isinstance(values, (list, tuple)):
        # Raise TypeError when the collection has the wrong type.
        raise TypeError("average() requires a list or tuple.")
    # Check that the collection contains at least one value.
    if not values:
        # Raise ValueError because an empty collection has no average.
        raise ValueError("Cannot calculate the average of an empty collection.")
    # Validate every item in the collection.
    for value in values:
        # Check whether the current item is numeric.
        if not isinstance(value, (int, float)):
            # Raise TypeError for an invalid item.
            raise TypeError("All values must be numeric.")
    # Start the running total at zero.
    total = 0
    # Loop through every value.
    for value in values:
        # Add the current value to the total.
        total += value
    # Return total divided by the number of values.
    return total / len(values)
