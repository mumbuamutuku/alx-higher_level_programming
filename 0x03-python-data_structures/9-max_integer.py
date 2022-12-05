#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0] 
    if len(my_list) == 0:
        return (None)
    else:
        for x in my_list:
            if x > max:
                max = x
        return (max)
