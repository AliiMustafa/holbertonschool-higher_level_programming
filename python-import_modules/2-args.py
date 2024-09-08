#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments.")
    else:
        if num == 1:
            print("{} argument:".format(num))
        else:
            print("{} arguments:".format(num))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
