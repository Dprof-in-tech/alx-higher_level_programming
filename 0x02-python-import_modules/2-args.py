#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    if len(argv) == 1:
        print("0 arguments.")
    else:
        print('{} arguments.'.format(len(argv) - 1), end='')
        num_arguments = len(argv) - 1
        if num_arguments > 1:
            print("{} argument{}:".format(num_arguments, 's'))
        else:
            print('')
        for index, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(index, arg))
