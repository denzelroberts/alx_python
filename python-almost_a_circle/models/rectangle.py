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
        """ finds width """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """ finds height """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """ finds x """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """ finds y """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value