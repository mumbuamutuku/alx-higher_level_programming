#!/usr/bin/python3
# 6-print_comb3.py
for n in range(89):
    if n / 10 < n % 10:
        print("{:02d}".format(n), end=", ")
print("{:02}".format(n+1))
