"""This is size of a function"""
def inherits_from(obj, a_class):
    """This is a function"""
    # return issubclass(obj,a_class())
    return issubclass(obj, a_class()) and type(obj) == a_class()
