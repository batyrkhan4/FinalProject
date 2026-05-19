import unittest
from core.functions import add, subtract, multiply, divide, square


class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_square(self):
        self.assertEqual(square(4), 16)


if __name__ == "__main__":
    unittest.main()