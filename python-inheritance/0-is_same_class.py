"""This is size of a function"""
def is_same_class(obj, a_class):
    """This is size of a function"""
    if type(obj) == type(a_class):
        return True
    elif isinstance(obj, a_class) == isinstance(obj, a_class):
        return False

# a = 1
# if is_same_class(a, int):
#     print("{} is an instance of the class {}".format(a, int.__name__))
# if is_same_class(a, float):
#     print("{} is an instance of the class {}".format(a, float.__name__))
# if is_same_class(a, object):
#     print("{} is an instance of the class {}".format(a, object.__name__))

