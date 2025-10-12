# Test script provided by the task
import sys

# Attempt to import the required class
try:
    from class_static_methods_demo import Calculator
except ImportError:
    print("Error: Could not import Calculator class. Check file existence.")
    sys.exit(1)

def main():
    """
    Demonstrates calling a static method and a class method directly 
    from the class name.
    """

    # Using the static method (called directly from the class)
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method (called directly from the class)
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
