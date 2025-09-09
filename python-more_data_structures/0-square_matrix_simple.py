#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []   # this will be the new matrix

    for row in matrix:               # loop through each row
        new_row = []                 # new row to store squared values
        for num in row:              # loop through each number in the row
            new_row.append(num ** 2) # square the number
        copy.append(new_row)         # add the new row to the new matrix

    return copy
