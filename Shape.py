"""
Author: Eitan Shoshan
Date: 02/10/2024
"""


class Shape:
    def __init__(self, area=0, perimeter=0, color=""):
        """
           creates shape object
        """
        self.area = area
        self.perimeter = perimeter
        self.color = color

    def set_color(self, color):
        """
           sets the color of the shape
        """
        self.color = color

    def get_color(self):
        """
           Gets the color of the shape
        """
        return self.color

    def get_area(self):
        """
           Gets the area of the shape
        """
        return self.area

    def get_perimeter(self):
        """
            Gets the perimeter of the shape
        """
        return self.perimeter


x = Shape()
x.set_color("orange")
assert x.get_color() == "orange"
