#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")

    if len(sys.argv) == 2:
        print("1 argument:")

        for i in range(len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

    if len(sys.argv) > 2:
        print(len(sys.argv) - 1, "arguments:")

        for i in range(len(sys.argv) - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))