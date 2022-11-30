#!/usr/bin/python3
# 5-print_comb2.py
for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{:02}".format(n), end=", ")
