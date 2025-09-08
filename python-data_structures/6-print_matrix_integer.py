#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:                 # each row is a list
        for j in range(len(row)):      # j is the index inside that row
            if j == len(row) - 1:      # last element
                print("{:d}".format(row[j]), end="")
            else:                      # not the last
                print("{:d}".format(row[j]), end=" ")
        print()  # move to next line after finishing the row
