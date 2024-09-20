import unittest

class TestExample(unittest.TestCase):

    def test_very_simple_test(self):
        # Setup
        a = 3
        b = 3

        # Assertion
        self.assertEqual(a, b)

    def test_another_very_simple_test(self):
        # Setup
        a = 3
        b = 3

        # Assertion
        self.assertTrue(a, b)

    def test_max(self):
        # Setup
        a = 5
        b = 10

        # Code Under Test
        actual = max(a, b)
        expected = 10

        # Assertion
        self.assertEqual(expected, actual)

    def test_min(self):
        # Setup
        a = 5
        b = 10

        # Code Under Test
        actual = min(a, b)
        expected = 5

        # Assertion
        self.assertEqual(expected, actual)
