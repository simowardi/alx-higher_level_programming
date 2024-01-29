#!/usr/bin/python3
""" Module rectangle """


class Rectangle:
    """
        A class that defines a rectangle
        from 4-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """
            Instantiation with optional width
            and height of the recctangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
            get of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            set of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            get of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            set of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
            Returns the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Returns the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        w_2 = self.__width * 2
        h_2 = self.__height * 2
        return w_2 + h_2

    def __str__(self):
        """
            prints the rectangle using print() or str()
        """
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return ("")
        for i in range(height):
            for j in range(width):
                print("#", end="")
            if i != height - 1:
                print('')
        return ("")

    def __repr__(self):
        """
            returns a string representation that could be
            used to recreate the object
        """
        return f"Rectangle{self.__width, self.__height}"

    def __del__(self):
        """
           delete an instance and prints a message
        """
        self.__width -= 1
        self.__height -= 1
        print("Bye rectangle...")
