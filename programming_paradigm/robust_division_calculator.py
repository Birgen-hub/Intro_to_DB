def safe_divide(numerator, denominator):
    """
    Performs division and robustly handles ZeroDivisionError and ValueError.

    Args:
        numerator (str): The numerator, expected as a string from command line.
        denominator (str): The denominator, expected as a string from command line.

    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Attempt to convert command line arguments to floating-point numbers
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den

        # Format the output as specified in the expected behavior
        return f"The result of the division is {result}"

    except ValueError:
        # Catches errors if the conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Catches errors if the denominator is 0
        return "Error: Cannot divide by zero."
