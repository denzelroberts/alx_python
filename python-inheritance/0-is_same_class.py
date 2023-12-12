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
    return isinstance(obj, a_class)

    
    # elif isinstance(obj, a_class) == False:
    #     return False
    
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
