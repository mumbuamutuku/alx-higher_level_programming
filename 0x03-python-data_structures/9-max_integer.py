#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if not my_list:
        return (None)
    for x in my_list:
        if x > max:
            max = x
    return (max)
