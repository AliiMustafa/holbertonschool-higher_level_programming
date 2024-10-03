#!/usr/bin/python3
"""Module for pascal triangle"""


def pascal_triangle(n):
    """Function for pascal triangle"""
    if n <= 0:
        return []

    result = []
    for i in range(n):
        pascal = []
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal.append(1)
            else:
                pascal.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(pascal)

    return result
