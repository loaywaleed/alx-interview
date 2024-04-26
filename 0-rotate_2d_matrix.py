#!/usr/bin/python3
"""
Rotate 2d matrix module
"""


def rotate_2d_matrix(matrix):
    """rotating 2d matrix in place"""

    for i in range(len(matrix)):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
