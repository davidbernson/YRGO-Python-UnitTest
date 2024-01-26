import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_computeAreaWithRadius1(self):
        circle = Circle(1)

        actual = circle.compute_area()

        self.assertAlmostEqual(3.14, actual, delta=0.1)

    def test_computeAreaWithRadius2(self):
        circle = Circle(2)

        actual = circle.compute_area()

        self.assertAlmostEqual(12.56, actual, delta=0.1)