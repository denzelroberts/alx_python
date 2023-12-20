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

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height
    
    #Display 0
    def display(self):
        """ print with '#' """
         # Display 1
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    #__str__
    def __str__(self):
        """ prints string"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)
           
    
    #Update #0
    def update(self, *args, **kwargs):
        """ updating rectangle """
        if len(args) != 0:
            i = 0
            rect_attrs = ["id", "width", "height", "x", "y"]
            for arg in args:
                setattr(self, rect_attrs[i], args[i])
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of rectangle """
        rect_dict = {}
        rect_attrs = ["id", "width", "height", "x", "y"]
        for attr in rect_attrs:
            rect_dict[attr] = getattr(self, attr)
        return rect_dict

