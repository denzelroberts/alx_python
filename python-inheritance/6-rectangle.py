# """This is a class"""
# class BaseGeometry:
#     """These are the attributes"""
#     def area(self):
#         """This is a function"""
#         raise Exception("area() is not implemented")
    
#     def integer_validator(self, name, value):
#         if type(value) != int:
#             raise TypeError("{} must be an integer".format(name))
        
#         if value <= 0:
#             raise ValueError("{} must be greater than 0".format(name))
        
# """This is a class"""        
# class Rectangle(BaseGeometry):
#     """These are the attributes"""
#     def __init__(self, width, height):
#         """validate that"""
#         self.integer_validator("width", width)
#         self.integer_validator("height", height)

#         """privatize"""
#         self.__width = width
#         self.__height = height

"""contains subclass Rectangle
which inherits from class BaseGeometry """

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class Rectangle """

    def __init__(self, width, height):
        """ initializes empty Rectangle and
        validates width and height as positive integers"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height