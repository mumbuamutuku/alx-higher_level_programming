#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict2 = {}
    for key in a_dictionary:
        dict2.update({key: a_dictionary[key] * 2})
    return dict2
