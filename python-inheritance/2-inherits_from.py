"""This is size of a function"""
def inherits_from(obj, a_class):
    """This is a function"""
    # return issubclass(obj,a_class())
    return type(obj) == a_class() and issubclass(obj, a_class())
