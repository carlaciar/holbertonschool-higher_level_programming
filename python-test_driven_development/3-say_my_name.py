#!/usr/bin/python3
"""
Print a full name as: 'My name is <first name> <last name>'.
"""


def say_my_name(*args):
    """
    Accepts 1 or 2 positional args: first_name [, last_name].
    Prints "My name is <first_name> <last_name>".
    """
    argc = len(args)
    if argc == 0:
        # Match CPython's 2-missing-args wording
        raise TypeError(
            "say_my_name() missing 2 required positional arguments: "
            "'first_name' and 'last_name'"
        )
    if argc == 1:
        first_name = args[0]
        last_name = ""
    elif argc == 2:
        first_name, last_name = args
    else:
        raise TypeError(
            "say_my_name() takes from 1 to 2 positional arguments "
            "but {} were given".format(argc)
        )

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {} ".format(first_name))  # trailing space required
    else:
        print("My name is {} {}".format(first_name, last_name))
