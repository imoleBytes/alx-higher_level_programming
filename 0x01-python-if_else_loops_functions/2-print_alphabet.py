#!/usr/bin/python3

for i in range(26):
    ascii_value = i + ord("a")
    alph = chr(ascii_value)
    print(alph, end="")
    # print("{:s}".format(chr(char + ord("a"))), end="")
