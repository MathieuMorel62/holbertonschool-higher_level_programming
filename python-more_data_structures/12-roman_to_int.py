#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_value = 0
    roman_list = list(roman_string)

    for i in roman_list:
        if i in roman_dict:
            value = roman_dict[i]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value = value
    return result
