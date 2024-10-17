"""
Author: Eitan Shoshan
Date: 02/10/2024
"""
from Shape import Shape


class Square(Shape):
    def __init__(self, length, color=""):
        """
            Creates square object
        """
        super().__init__(color)
        self.length = length

    def get_length(self):
        """
            Gets the length of the square
        """
        return self.length

    def get_area(self):
        """
            Gets the area of the square
        """
        return self.length ** 2

    def get_perimeter(self):
        """
            Gets the perimeter of the square
        """
        return self.length * 4

    def __add__(self, other):
        """
            Creates a new object that is the addition of the two objects
        """
        return Shape(self.get_area() + other.get_area(), self.get_perimeter() + other.get_perimeter())


y = Square(8)
assert y.get_length() == 8
assert y.get_area() == 64
assert y.get_perimeter() == 32
