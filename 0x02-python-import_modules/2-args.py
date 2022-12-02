#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    argv = sys.argv[1:]
    len = len(argv)
    count = 1
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(len))
        while count <= len:
            print("{}: {}".format(count, sys.argv[count]))
            count += 1
