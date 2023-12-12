"""This is size of a class"""
class a_class:
    """This is size of a method"""
    pass

"""This is size of a class"""
class obj:
    """This is size of a method"""
    pass

def is_same_class(obj, a_class):
    """This is size of a function"""
    if isinstance(obj, a_class) == True:
        same_class = isinstance(obj, a_class)
        return same_class
    
    else:
        return False
