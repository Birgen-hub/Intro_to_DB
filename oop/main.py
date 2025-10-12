# Test script provided by the task
import sys
import math # math is needed for pi, though the result printing is handled by the class methods

# Attempt to import the required classes
try:
    from polymorphism_demo import Shape, Rectangle, Circle
except ImportError:
    print("Error: Could not import classes from polymorphism_demo.py. Check file existence.")
    sys.exit(1)

def main():
    """
    Demonstrates polymorphism by iterating over a list of different shapes 
    and calling the area() method on each.
    """
    # Create a list of different Shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the list. The same method call (shape.area()) 
    # produces different behavior based on the object's type (polymorphism).
    for shape in shapes:
        # Use __class__.__name__ to dynamically get the type of shape being processed
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
