#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize object's attribute
        args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set/get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "set/get the height of the Rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "set/get the x coordinate of the Rectangle"
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "set/get the y coordinate of the Rectangle"
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area Method
        calculate the rectangle object's area
        """
        return self.__width * self.__height

    def display(self):
        """display a representation of the Rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            print('#' * self.__width)

    def __str__(self):
        """__str__ method
        print the rectangle on print() or str()
        """
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'\
            f' - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        """Update Rectangle
        args:
            *args (int): new attribute values.
                - 1st arg id attribute
                - 2nd arg width attribute
                - 3rd arg height attribute
                - 4th arg x attribute
                - 5th arg y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if args:
            for i in range(len(args)):
                if i == 0 and args[i] is not None:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            if kwargs:
                for k, v in kwargs.items():
                    if k == "id" and v is not None:
                        self.id = v
                    elif k == "width":
                        self.width = v
                    elif k == "height":
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        my_dic = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return my_dic
