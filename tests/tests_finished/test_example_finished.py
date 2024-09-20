import unittest

class TestExample(unittest.TestCase):
    
    def test_verySimpleTest(self):
        # Setup
        a = 3
        b = 3

        # Assertion
        self.assertEqual(a, b)

    def test_anotherVerySimpleTest(self):
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

