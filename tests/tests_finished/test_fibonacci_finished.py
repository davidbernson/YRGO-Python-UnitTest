import unittest
from parameterized import parameterized_class
from fibonacci import Fibonacci

# Decorate as parameterized_class, including test values and expected results for some values of the fibonacci function
@parameterized_class(('n', 'expected'), [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (20, 6765),
        (30, 832040),
        (35, 9227465)
    ])
class TestFibonacci(unittest.TestCase):
    # Add class variables for the @parameterized_class to prevent linting issues
    n = None
    expected = None

    def setUp(self):
        self.fibo = Fibonacci()

    def test_fibonacci_recursive(self):
        self.assertEqual(self.expected, self.fibo.fibonacci_recursive(self.n))

    def test_fibonacci_math(self):
        self.assertAlmostEqual(self.expected, self.fibo.fibonacci_math(self.n), delta=0.001)

    def tearDown(self):
        self.fibo = None
