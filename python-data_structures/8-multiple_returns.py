#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        f = None
    f = sentence[0]
    l = len(sentence)
    return l, f