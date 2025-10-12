class Calculator:
    """
    A class demonstrating the use and distinction between static methods 
    and class methods.
    """

    # Class Attribute: Accessible by class methods via the 'cls' parameter
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Returns the sum of two numbers. 
        It does not require access to the instance (self) or the class (cls).
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Returns the product of two numbers.
        It receives the class itself (cls) as the first argument, allowing it 
        to access and use class attributes like calculation_type.
        """
        # Accessing the class attribute via the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Note: No main function is needed here, as the classes are imported by main.py
