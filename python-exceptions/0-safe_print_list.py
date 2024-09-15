#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for i in my_list:
            if x <= 0:
                break
            print(f"{i}", end="")
            a += 1
            x -= 1
        print()
    except Exception:
        return 0
    else:
        return a
