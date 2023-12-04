from sys import argv

if __name__ == "__main__":
    length_of_args = len(argv) - 1
    if length_of_args == 0:
        print("{}".format("0 arguments."))
    elif length_of_args == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(length_of_args, "arguments:"))
        for i in range(1, length_of_args + 1):
            print("{:d}: {}".format(i, argv[i]))

# import sys

# sys.argv[0]

# if len(sys.argv) > 1:
#     print("there are", len(sys.argv)-1, "arguments:")
#     for arg in sys.argv[1:]:
#         print(arg)
# else:
#     print("0 arguments.")