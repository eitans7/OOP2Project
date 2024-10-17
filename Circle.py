"""
Author: Eitan Shoshan
Date: 02/10/2024
"""
from Shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius, color=""):
        """
            Creates circle object
        """
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        """
            Gets the area of the circle
        """
        return math.pi * (self.radius ** 2)

    def get_perimeter(self):
        """
            Gets the perimeter of the circle
        """
        return math.pi * 2 * self.radius


f = Circle(5)
assert f.get_perimeter() == 2 * math.pi * f.radius
assert f.get_area() == math.pi * f.radius ** 2
