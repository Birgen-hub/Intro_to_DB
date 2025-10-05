import sys

# Attempt to import the safe_divide function
try:
    from robust_division_calculator import safe_divide
except ImportError:
    print("Error: Could not import safe_divide. Ensure robust_division_calculator.py is in the directory.")
    sys.exit(1)

def main():
    """
    Handles command line arguments and calls the safe_divide function.
    """
    # Check for the correct number of arguments (script name + numerator + denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # sys.argv[0] is the script name, [1] is numerator, [2] is denominator
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the robust division function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
