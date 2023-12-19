#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
        try:
            int_value = int(value)
            print("{:d}".format(int_value))
            return True
        except (ValueError, TypeError) as e:
            sys.stderr.write("Exception: {}".format(e))
            return False
