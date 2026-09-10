# Create a custom exception for unsupported operations or conversions.
class InvalidOperationError(Exception):
    """Represent an operation or conversion that is not supported."""
    # No additional behavior is needed because Exception provides it.
    pass
