import unittest
import math


class TestSimpleMath(unittest.TestCase):
    
    def setUp(self):
        self.a = 10
        self.b = 3

    def test_addition(self):
        # Code Under Test
        actual = self.a + self.b
        expected = 13

        # Assertion
        self.assertEqual(expected, actual)

    def test_subtraction(self):
        # Code Under Test
        actual = self.a - self.b
        expected = 7

        # Assertion
        self.assertEqual(expected, actual)

    def test_division(self):
        # Code Under Test
        actual = self.a / self.b
        expected = 3.3

        # Assertion
        self.assertAlmostEqual(expected, actual, delta=0.05)
