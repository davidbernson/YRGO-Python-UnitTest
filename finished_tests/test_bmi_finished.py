import unittest
from computeBMI import computeBMI, computeBMI2

class TestPerson(unittest.TestCase):
    
    def test_computeBMI_200cm100kg(self):
        # Setup
        weight_kg = 100
        length_m = 2.0

        # Code Under Test
        actual = computeBMI(weight_kg, length_m)
        expected = 25.0

        # Assertion
        self.assertEqual(expected, actual)

    def test_computeBMI2_200cm100kg(self):
        # Setup
        weight_kg = 100
        length_m = 2.0

        # Code Under Test
        actual = computeBMI2(weight_kg, length_m)
        expected = 25.0

        # Assertion
        self.assertEqual(expected, actual)