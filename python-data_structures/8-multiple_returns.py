#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        f = None
    else:
        f = sentence[0]
    ln = len(sentence)
    return ln, f
