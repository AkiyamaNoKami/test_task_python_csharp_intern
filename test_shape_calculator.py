import unittest
from shape_calculator import ShapeCalculator

class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.circle_area(0), 0)
        self.assertAlmostEqual(ShapeCalculator.circle_area(1), 3.141592653589793)
        self.assertAlmostEqual(ShapeCalculator.circle_area(5), 78.53981633974483)

    def test_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(6, 8, 10), 24)
        self.assertAlmostEqual(ShapeCalculator.triangle_area(7, 8, 9), 26.832815729997478)

    def test_is_right_triangle(self):
        self.assertTrue(ShapeCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(ShapeCalculator.is_right_triangle(5, 6, 7))
        self.assertTrue(ShapeCalculator.is_right_triangle(5, 12, 13))

if __name__ == '__main__':
    unittest.main()
