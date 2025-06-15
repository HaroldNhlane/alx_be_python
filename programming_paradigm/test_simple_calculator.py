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
    def test_addition(self):
        """Test the addition method with various number types and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(0.5, 0.5), 1.0)

        # Negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, -20), -30)

        # Positive and negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -3), 2)
        self.assertEqual(self.calc.add(-7, 2), -5)

        # With zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

        # Floating-point numbers (use assertAlmostEqual for precision)
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(1.23, 4.56), 5.79)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)


    # --- Test Methods for subtract() ---
    def test_subtraction(self):
        """Test the subtraction method with various number types and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(10, 20), -10)

        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-3, -5), 2)

        # Positive and negative numbers
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)

        # With zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        # Floating-point numbers
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(10.0, 0.1), 9.9)


    # --- Test Methods for multiply() ---
    def test_multiplication(self):
        """Test the multiplication method with various number types and scenarios."""
        # Positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 10), 100)

        # Negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

        # Positive and negative numbers
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)

        # With zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

        # Floating-point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)


    # --- Test Methods for divide() ---
    def test_divide_numbers(self):
        """Test the divide method with various number types and scenarios (excluding division by zero)."""
        # Positive numbers
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)

        # Negative numbers
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        self.assertEqual(self.calc.divide(-7, -2), 3.5)

        # Mixed signs
        self.assertEqual(self.calc.divide(10, -5), -2.0)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)

        # Zero by non-zero number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -5), -0.0) # Floats can have negative zero

        # Floating-point numbers
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

    def test_divide_by_zero(self):
        """Test division by zero, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Edge case: 0/0 is also None per the function's logic


# This block allows you to run the tests directly from the command line
if __name__ == '__main__':
    # unittest.main() looks at sys.argv, and the first argument is normally the script name.
    # We pass a dummy first argument to ensure unittest.main() doesn't try to interpret
    # test_simple_calculator.py as a test name itself, and exit=False prevents it from
    # exiting sys immediately, which can be useful in some IDEs.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)