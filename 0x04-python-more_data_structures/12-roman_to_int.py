#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string:
        roman_ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
        roman_ref['M'] = 1000
        minsum = 0
        retsum = 0
        curr_v = 0
        for c in roman_string:
            rom_v = roman_ref[c]
            if rom_v > curr_v:
                rom_v -= minsum
                retsum -= minsum
                minsum = 0
            retsum += rom_v
            minsum += rom_v
            curr_v = rom_v
        return retsum
    else:
        return 0
