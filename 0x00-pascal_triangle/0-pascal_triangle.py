#!/usr/bin/python3
"""
Module that returns pascal triangle values depending on new_array
"""


def pascal_triangle(n):
    """Function that returns pascal triangle list"""
    test_array = [0, 1, 0]
    final = []
    if n <= 0:
        return []
    final.append([1])
    while n > 1:
        new_array = [ (test_array[i] + test_array[i - 1]) for i in range(1, len(test_array)) ]
        final.append(new_array)
        test_array = [0, *new_array, 0]
        n -= 1
    return final
