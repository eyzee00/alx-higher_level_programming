#!/usr/bin/python3
def roman_to_int(s):
    if s is None:
        return 0
    roman_d = {
            "I" : 1, "V" : 5, "X": 10,
            "L" : 50, "C" : 100, "D" : 500,
            "M" : 1000
            }
    converted_res = 0
    i = 0
    while i < len(s):
        clause1 = bool(i + 1 < len(s))
        clause2 = bool(roman_d[s[i]] < roman_d[s[i + 1]])
        if clause1 and clause2:
            converted_res -= roman_d[s[i]]
        else:
            converted_res += roman_d[s[i]]
        i += 1
    return int(converted_res)
