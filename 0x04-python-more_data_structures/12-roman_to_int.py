#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0
    
    roman_string = roman_string.upper()
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    prev = roman_values[roman_number[0]]

    for i in roman_string:
        if i in list(roman_values.keys()):
            total += roman_values[i]
            if prev < roman_values[i]:
                total -= prev * 2
            prev = roman_values[i]
        else:
            return 0
    return total
