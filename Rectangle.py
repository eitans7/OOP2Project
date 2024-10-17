"""
Author: Eitan Shoshan
Date: 02/10/2024
"""
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, height, length, color=""):
        """
            Creates rectangle object
        """
        super().__init__(color)
        self.length = length
        self.height = height

    def get_length(self):
        """
            Gets the length of the rectangle
        """
        return self.length

    def get_height(self):
        """
            Gets the height of the rectangle
        """
        return self.height

    def get_area(self):
        """
            Gets the area of the rectangle
        """
        return self.length * self.height

    def get_perimeter(self):
        """
            Gets the perimeter of the rectangle
        """
        return self.height * 2 + self.length * 2

    def __add__(self, other):
        """
            Creates a new object that is the addition of the two objects
        """
        return Shape(self.get_area() + other.get_area(), self.get_perimeter() + other.get_perimeter())


e = Rectangle(7, 3)
assert e.get_area() == 21
assert e.get_height() == 7
assert e.get_length() == 3
assert e.get_perimeter() == 20
