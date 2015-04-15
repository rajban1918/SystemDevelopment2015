import unittest

import calculator_functions as calc

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 3

    def test_add(self):
        self.assertEqual(calc.add(self.x, self.y), 5)

    def test_subtract_neg(self):
        self.assertEqual(calc.subtract(self.x, self.y), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(self.x, self.y), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(self.y, self.x), 1.5)

if __name__ == "__main__":
    unittest.main()
