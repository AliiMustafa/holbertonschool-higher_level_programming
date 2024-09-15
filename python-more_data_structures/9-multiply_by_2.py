#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i, j in a_dictionary.items():
        j *= 2
        new_dic[i] = j
    return new_dic
