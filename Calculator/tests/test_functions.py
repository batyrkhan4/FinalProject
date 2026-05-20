import unittest
from core.validators import is_valid_number
from models.operation import BinaryOperation, ScientificOperation
from core.functions import (
    square,
    cube,
    inverse,
    square_root,
    cube_root,
    absolute,
    ten_power,
    two_power,
    natural_log,
    common_log,
    exponent,
    factorial_num,
    sine,
    cosine
)


class TestCalculatorFunctions(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_cube(self):
        self.assertEqual(cube(3), 27)

    def test_inverse(self):
        self.assertEqual(inverse(2), 0.5)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_cube_root(self):
        self.assertAlmostEqual(cube_root(27), 3)

    def test_absolute(self):
        self.assertEqual(absolute(-10), 10)

    def test_ten_power(self):
        self.assertEqual(ten_power(2), 100)

    def test_two_power(self):
        self.assertEqual(two_power(3), 8)

    def test_natural_log(self):
            self.assertAlmostEqual(natural_log(1), 0)

    def test_common_log(self):
        self.assertEqual(common_log(100), 2)

    def test_exponent(self):
        self.assertAlmostEqual(exponent(1), 2.718281828459045)

    def test_factorial_num(self):
        self.assertEqual(factorial_num(5), 120)

    def test_sine(self):
        self.assertAlmostEqual(sine(90), 1)

    def test_cosine(self):
        self.assertAlmostEqual(cosine(0), 1)


    def test_valid_number(self):
        self.assertTrue(is_valid_number("25"))
        self.assertTrue(is_valid_number("-3.5"))
        self.assertFalse(is_valid_number("abc"))

    
    def test_binary_operation(self):
        operation = BinaryOperation("2+2", 4)
        self.assertEqual(operation.get_expression(), "2+2")
        self.assertEqual(operation.get_result(), 4)


    def test_scientific_operation(self):
        operation = ScientificOperation("sin", 90, 1)
        self.assertEqual(operation.get_expression(), "sin(90)")
        self.assertEqual(operation.get_result(), 1)
if __name__ == "__main__":
    unittest.main()