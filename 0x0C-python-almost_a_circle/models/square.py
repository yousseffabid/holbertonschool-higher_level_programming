#!/usr/bin/python3
"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize object's attribute
        args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method
        print the rectangle on print() or str()
        """
        return f'[Square] ({self.id}) {self.x}/{self.y}'\
            f' - {self.width}'

    @property
    def size(self):
        """get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
                if key == "id":
                    self.id = kwargs[key]

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
