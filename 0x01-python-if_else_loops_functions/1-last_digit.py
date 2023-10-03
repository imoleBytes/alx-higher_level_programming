#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
# number = 7206

if number < 0:
    number = -1 * number
    last_digit = (number % 10) * -1
else:
    last_digit = number % 10

str = f"Last digit of {number} is {last_digit}"

if last_digit < 6 and last_digit != 0:
    print(f"{str} and is less than 6 and not 0")
elif last_digit == 0:
    print(f"{str} and is 0")
else:
    print(f"{str} and is greater than 5")
