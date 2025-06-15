import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, covering basic arithmetic operations
    and edge cases.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    # --- Test Methods for add() ---
    def test_add_positive_numbers(self):
        """Test addition with two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0.5, 0.5), 1.0)

    def test_add_negative_numbers(self):
        """Test addition with two negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, -20), -30)

    def test_add_positive_and_negative_numbers(self):
        """Test addition with a positive and a negative number."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

    def test_add_with_zero(self):
        """Test addition where one or both numbers are zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_add_float_numbers(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.23, 4.56), 5.79)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Use assertAlmostEqual for floats

    # --- Test Methods for subtract() ---
    def test_subtract_positive_numbers(self):
        """Test subtraction with two positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 20), -10)
        self.assertEqual(self.calc.subtract(5.0, 3.0), 2.0)

    def test_subtract_negative_numbers(self):
        """Test subtraction with two negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, -20), 10)

    def test_subtract_positive_and_negative_numbers(self):
        """Test subtraction with a positive and a negative number."""
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_with_zero(self):
        """Test subtraction where one or both numbers are zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_float_numbers(self):
        """Test subtraction with floating-point numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(10.0, 0.1), 9.9)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2)


    # --- Test Methods for multiply() ---
    def test_multiply_positive_numbers(self):
        """Test multiplication with two positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiply_negative_numbers(self):
        """Test multiplication with two negative numbers."""
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_multiply_positive_and_negative_numbers(self):
        """Test multiplication with a positive and a negative number."""
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)

    def test_multiply_with_zero(self):
        """Test multiplication where one or both numbers are zero."""
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_float_numbers(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.3), 0.03)


    # --- Test Methods for divide() ---
    def test_divide_positive_numbers(self):
        """Test division with two positive numbers."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        """Test division with two negative numbers."""
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        self.assertEqual(self.calc.divide(-7, -2), 3.5)

    def test_divide_positive_by_negative(self):
        """Test division of a positive by a negative number."""
        self.assertEqual(self.calc.divide(10, -5), -2.0)

    def test_divide_negative_by_positive(self):
        """Test division of a negative by a positive number."""
        self.assertEqual(self.calc.divide(-10, 5), -2.0)

    def test_divide_by_zero(self):
        """Test division by zero, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Edge case: 0/0 is also None per the function's logic

    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), -0.0) # Floats can have negative zero

    def test_divide_float_numbers(self):
        """Test division with floating-point numbers."""
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)


# This block allows you to run the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)