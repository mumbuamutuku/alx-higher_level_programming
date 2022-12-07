#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = []
    [res.append(x) for x in set_2 if x not in set_1]
    [res.append(x) for x in set_1 if x not in set_2]
    return res
