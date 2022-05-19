"""
General library for areas of geometric plane figures.

a = circle_area(diameter)
a = rectangle_area(length, width)
a = square_area(side)
"""
from math import pi

ANIMAL = 'wombat'

def circle_area(diameter):
    """
    Calculate area of circle from diameter

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    """
    Calculate area of rectangle.

    :param length: Length of one side
    :param width: Length of other side
    :return: Area of rectangle
    """
    return length * width

def square_area(side):
    """
    Calculate area of square.

    :param side: Length of one side
    :return: Area of side
    """
    return side ** 2


