#!/usr/bin/python3

for i in range(99):
    print("{}".format('0' + str(i) if i < 10 else i), end=", ")
print(99)
