#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        num_arguments = len(argv) - 1
        print('{} argument{}{}'.format(
            num_arguments,
            's' if num_arguments > 1 else '',
            ':' if num_arguments > 0 else '.'
            ))
    for index, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(index, arg))
