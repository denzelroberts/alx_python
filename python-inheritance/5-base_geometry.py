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