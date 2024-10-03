#!/usr/bin/python3
"""Module for pascal triangle"""


def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)


def combin(a, b):
    result = fact(a) / (fact(b) * fact(a - b))
    return result


def pascal_triangle(n):
    if n <= 0:
        return []
    for i in range(n):
        pascal = []
        for j in range(i + 1):
            pascal.append(int(combin(i, j)))
        print(pascal)
