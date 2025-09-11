#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")  # print without newline
            count += 1
    except IndexError:
        pass  # stop if list runs out
    print()  # new line after printing
    return count
