#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_num(n):
        return n * n
    new_list = []
    for x in matrix:
        new_list.append(list(map(square_num, x)))
    return new_list
