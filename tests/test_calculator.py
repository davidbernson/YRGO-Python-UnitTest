import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.actual = self.calculator.add(8, 3)
        self.expected = 11

        self.assertEqual(self.expected, self.actual)

    def test_subtraction(self):
        self.actual = self.calculator.subtract(8, 3)
        self.expected = 5

        self.assertEqual(self.expected, self.actual)

    def test_power(self):
        self.actual = self.calculator.power(8, 3)
        self.expected = 512

        self.assertEqual(self.expected, self.actual)

    def tearDown(self):
        self.calculator = None
