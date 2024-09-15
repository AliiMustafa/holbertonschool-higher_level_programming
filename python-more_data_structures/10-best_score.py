#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] == max(list(a_dictionary.values())):
            return i
