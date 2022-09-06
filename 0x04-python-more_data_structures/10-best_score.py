#!/usr/bin/python3
def best_score(a_dictionary):
    value = sorted(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == value[-1]:
            return key
        else:
            return "None"
