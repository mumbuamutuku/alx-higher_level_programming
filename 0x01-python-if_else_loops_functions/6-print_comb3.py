#!/usr/bin/python3
#5-print_comb2.py
for n in range(89):
	if n / 10 < n % 10:
		print("{:02d}".format(n), end=", ")
print("{:02}".format(n+1))
