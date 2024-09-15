#!/usr/bin/python3
def roman_digits(roman):
    roman_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return roman_to_value.get(roman, 0)


def roman_to_int(roman_string):
    sum = 0
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            return sum + roman_digits(roman_string[i])
        elif roman_digits(roman_string[i]) < roman_digits(roman_string[i + 1]):
            sum = sum - roman_digits(roman_string[i])
        else:
            sum = sum + roman_digits(roman_string[i])
