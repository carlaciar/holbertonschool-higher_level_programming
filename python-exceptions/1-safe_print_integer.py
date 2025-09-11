#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value % 1 == 0:
            print("{:d}".format(value))
            return True

        else:
            return False

    except TypeError:
        return False
