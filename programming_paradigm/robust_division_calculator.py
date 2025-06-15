def safe_divide(numerator, denominator):
    """
    Performs division of two numbers, handling potential ZeroDivisionError
    and ValueError (for non-numeric inputs).

    Args:
        numerator (str or float or int): The numerator for the division.
        denominator (str or float or int): The denominator for the division.

    Returns:
        str: A message indicating the result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        # Catch error if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."

    try:
        # Perform the division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # Catch error if division by zero occurs
        return "Error: Cannot divide by zero."