#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = [] 
    for x in my_list:
        if x % 2 == 0:
            multiple.append(True)
        else:
            multiple.append(False)
    return (multiple)    
