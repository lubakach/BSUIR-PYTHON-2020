from unittest import TestCase
from isp2lb.vectors import Vector


class TestNDimensionalVector(TestCase):
    def test_length(self):
        self.vector1 = Vector(12, 5)
        self.assertEqual(self.vector1.length(), 13.0)

    def test_wrong_length(self):
        self.vector2 = Vector(12, 5)
        self.assertNotEqual(self.vector2.length(), 15.0)
