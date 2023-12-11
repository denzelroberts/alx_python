"""This is size of a square"""
class Square:
    """class of the size of the square"""
    def __init__(self, size=0):
        """
        The initialization of size
        """
        self.__size = size

        if type(size) == int:
            size
        else:
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        """
        area of size
        """
        return self.__size ** 2

    @property 
    def size(self):
        """
        getter
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        setter
        """
        self.size = value