#!/usr/bin/python3

for i in range(26):
    if chr((i + ord("a"))) == "e" or chr((i + ord("a"))) == "q":
        continue
    print("{:s}".format(chr(i + ord("a"))), end="")
