#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    try:
        for i in my_list[:x]:
            try:
                print("{:d}".format(i), end='')
                counter += 1
            except (TypeError, ValueError):
                pass
        print('')
    except TypeError:
        pass
    return counter
