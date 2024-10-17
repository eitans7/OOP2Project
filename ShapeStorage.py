"""
Author: Eitan Shoshan
Date: 02/10/2024
"""
import random
from Rectangle import Rectangle
from Square import Square
from Circle import Circle
COLORS = ["blue", "red", "green", "yellow", "white", "black", "purple", "orange"]
TYPES = [Rectangle, Square, Circle]


class Container:
    def __init__(self):
        """
            Creates shapes container object
        """
        self.container = []

    def generate(self, x):
        """
            Generates x random shapes
        """
        for i in range(x):
            random_color = random.choice(COLORS)
            random_type = random.choice(TYPES)
            if random_type == Square:
                length = random.randrange(1, 11)
                square = random_type(length)
                square.set_color(random_color)
                self.container.append(square)
            elif random_type == Rectangle:
                height = random.randrange(1, 11)
                length = random.randrange(1, 11)
                rectangle = random_type(height, length)
                rectangle.set_color(random_color)
                self.container.append(rectangle)
            else:
                radius = random.randrange(1, 11)
                circle = random_type(radius)
                circle.set_color(random_color)
                self.container.append(circle)

    def sum_areas(self):
        """
            Sum of areas
        """
        sum = 0
        for i in range(len(self.container)):
            sum += self.container[i].get_area()
        return sum

    def sum_perimeters(self):
        """
            Sum of perimeters
        """
        sum = 0
        for i in range(len(self.container)):
            sum += self.container[i].get_perimeter()
        return sum

    def count_colors(self):
        """
            Counts the colors
        """
        dic = {color: 0 for color in COLORS}
        for object_ in self.container:
            if object_.get_color() in dic:
                dic[object_.get_color()] += 1
        return dic


my_container = Container()
my_container.generate(100)
print("sum perimeter:", my_container.sum_perimeters())
print("sum area:", my_container.sum_areas())
print("colors:", my_container.count_colors())

assert type(my_container.count_colors()) == dict
