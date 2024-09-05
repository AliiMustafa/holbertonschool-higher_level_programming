#!/usr/bin/python3
for x in range(97, 123):
    if x == "q" or x == "e":
        continue
    print("{}".format(chr(x)), end="")
