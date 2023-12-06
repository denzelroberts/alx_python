def no_c(my_string):
    letter_c = my_string.translate({ord(i): None for i in 'cC'})
    return letter_c
