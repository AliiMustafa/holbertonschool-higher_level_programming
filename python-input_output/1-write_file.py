#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "x", encoding="utf-8") as f:
        data = f.write(text)
        return data
