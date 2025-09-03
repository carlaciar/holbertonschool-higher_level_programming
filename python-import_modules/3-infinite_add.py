#!/usr/bin/python3
import sys

total = 0

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            total += int(arg)
        print(total)
