#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Defines a Square class and methods for area and perimeter"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialises a Square object with given arguments"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns the square's dimensions (width/height)"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
