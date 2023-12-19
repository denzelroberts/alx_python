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