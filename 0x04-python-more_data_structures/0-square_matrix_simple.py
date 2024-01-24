#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# computes the square value of all integers of a matrix.
#
# (C) 2024 Silimwe Rodgers, Lusaka, Zambia
# email Silimwerodgers@gmail.com
# -----------------------------------------------------------


def square_matrix_simple(matrix=[]):
    new_matrix = [[number**2 for number in row] for row in matrix]
    return new_matrix
