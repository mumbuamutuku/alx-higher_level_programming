#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    argv = sys.argv[1:]
    len = len(argv)
    count = 1 
    sum = 0
    while count <= len:
        sum += int(sys.argv[count])
        count += 1
    print("{}".format(sum))
