#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    new_word = ""
    for i in str:
        if islower(i):
            new_word = new_word + chr(ord(i) - 32)
        else:
            new_word = new_word + i
    print("{}".format(new_word))
