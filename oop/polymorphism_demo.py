import math

class Shape:
    """
    Base class for shapes. Defines the area method which must be overridden.
    """
    def area(self):
        """
        Raises a NotImplementedError to enforce method overriding in derived classes.
        """
        raise NotImplementedError("Subclass must implement abstract method 'area'")


class Rectangle(Shape):
    """
    Derived class for a rectangle. Overrides the area method.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle: length * width."""
        return self.length * self.width


class Circle(Shape):
    """
    Derived class for a circle. Overrides the area method.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle: pi * radius^2."""
        # Use math.pi for precision
        return math.pi * (self.radius ** 2)

# Note: No main function is needed here, as the classes are imported by main.py
