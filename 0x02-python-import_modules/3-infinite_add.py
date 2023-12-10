#!/usr/bin/python3
from sys import argv


arguments = argv[1:]
if len(arguments) == 0:
    print("0")
else:
    total = sum(int(arg) for arg in arguments)
    print(total)
