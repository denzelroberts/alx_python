"""Importing a class"""
from models.base import Base

"""Creating rectangle class"""
class Rectangle(Base):
    """ defines class Square """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ function """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ checks width """
        return self.__width

    @width.setter
    def width(self, value):
        """ checks if width is a positive integer """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ checks height """
        return self.__height

    @height.setter
    def height(self, value):
        """ checks if height is a positive integer """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """ checks if x is a positive or zero integer """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ gets y """
        return self.__y

    @y.setter
    def y(self, value):
        """ checks if y is a positive or zero integer """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value