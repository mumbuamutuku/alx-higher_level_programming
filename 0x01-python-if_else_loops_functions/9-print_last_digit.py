#!/usr/bin/python3
def print_last_digit(num):

    digit = abs(num) % 10
    print(digit, end="")
    return digit
