#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    counter = 0

    for i in my_list:
        if counter == x:
            break

        try:
            print("{} ".format(i), end='')
            counter += 1
        except (RuntimeError, TypeError, NameError):
            pass

    print('')
    return counter
