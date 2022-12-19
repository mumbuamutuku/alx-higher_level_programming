#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    output = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            output += 1
        except IndexError:
            break
    print("")
    return (output)
