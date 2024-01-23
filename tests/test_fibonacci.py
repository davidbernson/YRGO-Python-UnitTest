import unittest
from parameterized import parameterized_class
from fibonacci import Fibonacci

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
        # (35, 9227465)
    ])
class TestFibonacci(unittest.TestCase):

    def test_fibonacci_recursive(self):
        self.fibo = Fibonacci()

        self.assertEqual(self.expected, self.fibo.fibonacci_recursive(self.n))
        # for n in range(10):
        #     with self.subTest(i=n):
        #         self.assertEqual(self.fibo.fibonacci_recursive(n), expected[n])

    def test_fibonacci_math(self):
        self.fibo = Fibonacci()

        self.assertAlmostEqual(self.expected, self.fibo.fibonacci_math(self.n), delta=0.001)

if __name__ == "__main__":
    unittest.main()