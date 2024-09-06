#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    for i in range(len(str)):
        if i == len(str) - 1:
            if islower(str[i]):
                print(chr(ord(str[i]) - 32))
            else:
                print(str[i])
        else:
            if islower(str[i]):
                print(chr(ord(str[i]) - 32), end="")
            else:
                print(str[i], end="")
