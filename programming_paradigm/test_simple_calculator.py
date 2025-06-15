import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Tests for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various numerical inputs.
        """
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)       # Mixed integers (negative and positive)
        self.assertEqual(self.calc.add(-5, -3), -8)     # Negative integers
        self.assertEqual(self.calc.add(0, 7), 7)        # Addition with zero
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)  # Floating point numbers
        self.assertEqual(self.calc.add(10, 0), 10)      # Adding zero
        self.assertEqual(self.calc.add(-10, 5), -5)     # Negative result
        self.assertEqual(self.calc.add(1.2, 3.4), 4.6)  # Floating point numbers
        self.assertEqual(self.calc.add(0, 0), 0)        # Both zeros

    def test_subtraction(self):
        """
        Test the subtract method with various numerical inputs.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)       # Positive integers
        self.assertEqual(self.calc.subtract(3, 5), -2)      # Negative result
        self.assertEqual(self.calc.subtract(-5, -3), -2)    # Negative integers
        self.assertEqual(self.calc.subtract(10, 0), 10)     # Subtraction with zero
        self.assertEqual(self.calc.subtract(0, 7), -7)      # Subtraction from zero
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0) # Floating point numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)     # Mixed integers
        self.assertEqual(self.calc.subtract(0, 0), 0)       # Both zeros

    def test_multiplication(self):
        """
        Test the multiply method with various numerical inputs.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)       # Positive integers
        self.assertEqual(self.calc.multiply(-1, 5), -5)    # Negative result
        self.assertEqual(self.calc.multiply(-2, -3), 6)    # Both negative integers
        self.assertEqual(self.calc.multiply(0, 5), 0)       # Multiplication by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)       # Multiplication of zero
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)   # Floating point numbers
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0) # Floating point numbers
        self.assertEqual(self.calc.multiply(0, 0), 0)       # Both zeros

    def test_division(self):
        """
        Test the divide method with various numerical inputs, including edge cases.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Normal division
        self.assertEqual(self.calc.divide(7, 2), 3.5)       # Division with float result
        self.assertEqual(self.calc.divide(-10, 2), -5.0)   # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5.0)   # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5.0)   # Both negative
        self.assertEqual(self.calc.divide(0, 5), 0.0)      # Zero divided by non-zero
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)  # Floating point numbers

        # Edge case: Division by zero
        self.assertIsNone(self.calc.divide(10, 0))          # Expects None as per class definition
        self.assertIsNone(self.calc.divide(-5, 0))          # Test negative numerator with zero
        self.assertIsNone(self.calc.divide(0, 0))           # Test zero by zero (also None)
