import unittest

# Import the class we are testing from the accompanying script
try:
    from simple_calculator import SimpleCalculator
except ImportError:
    # Provide a helpful error if the import fails
    print("Error: Could not import SimpleCalculator. Ensure simple_calculator.py is present.")
    exit(1)

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class, covering all arithmetic operations
    and edge cases.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

    # --- Test Cases for Add Method ---
    def test_addition(self):
        """Test the addition method with various number types."""
        # Test positive integers
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -5), -6, "Should be -6")
        # Test positive and negative
        self.assertEqual(self.calc.add(10, -4), 6, "Should be 6")
        # Test floating-point numbers
        self.assertEqual(self.calc.add(0.5, 0.5), 1.0, "Should be 1.0")

    # --- Test Cases for Subtract Method ---
    def test_subtraction(self):
        """Test the subtraction method."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5")
        # Test result is negative
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5")
        # Test subtracting a negative number
        self.assertEqual(self.calc.subtract(5, -3), 8, "Should be 8")
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5, "Should be -5")

    # --- Test Cases for Multiply Method ---
    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(4, 5), 20, "Should be 20")
        # Test one negative number
        self.assertEqual(self.calc.multiply(-2, 6), -12, "Should be -12")
        # Test two negative numbers
        self.assertEqual(self.calc.multiply(-3, -3), 9, "Should be 9")
        # Test multiplication by zero
        self.assertEqual(self.calc.multiply(99, 0), 0, "Should be 0")
        # Test floating point
        self.assertAlmostEqual(self.calc.multiply(1.5, 2), 3.0, "Should be 3.0")

    # --- Test Cases for Divide Method ---
    def test_division_normal(self):
        """Test the division method under normal circumstances."""
        # Basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0, "Should be 5.0")
        # Division resulting in a float
        self.assertEqual(self.calc.divide(1, 4), 0.25, "Should be 0.25")
        # Division with negative numbers
        self.assertEqual(self.calc.divide(-10, 5), -2.0, "Should be -2.0")

    def test_division_by_zero(self):
        """Test the edge case: division by zero must return None."""
        # Division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
        self.assertIsNone(self.calc.divide(-5, 0), "Division by zero should return None")

if __name__ == '__main__':
    unittest.main()
