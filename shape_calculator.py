import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = sorted([side1, side2, side3])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-10

