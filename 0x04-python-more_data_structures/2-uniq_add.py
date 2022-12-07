#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_of_unique_num = []
    unique_num = set(my_list)
    for n in unique_num:
        list_of_unique_num.append(n)
    total = 0
    for x in range(len(list_of_unique_num)):
        total += list_of_unique_num[x]
    return total
