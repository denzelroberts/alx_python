"""This is a class"""
class BaseGeometry:
    """These are the attributes"""
    def area(self):
        """This is a function"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
"""This is a class"""        
class Rectangle(BaseGeometry):
    """These are the attributes"""
    def __init__(self, width, height):
        """validate that"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """privatize"""
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)