#!/usr/bin/python3
def uppercase(str):
    for char in str:
        letter = ord(char)

        if ord('a') <= letter <= ord('z'):
            letter = letter - 32

        print("{}".format(chr(letter)), end="")

    print()
