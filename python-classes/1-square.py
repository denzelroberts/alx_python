"""This is size of a square"""
class Square:
    """class of the size of the square"""
    def __init__(self, size=0):
        """
        The initialization of size
        """
        self.__size = size

        try:
            __size = int()
        except TypeError:
            print("size must be an integer")
        
        try:
            __size < 0
        except ValueError:
            print("size must be >=0")