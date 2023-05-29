#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    i = 0
    sum = 0
    for j in roman_string:
        if j == 'I':
            sum += 1
        elif j == 'V':
            if roman_string[i - 1] == 'I' and i != 0:
                sum -= 1
                sum += 4
            else:
                sum += 5
        elif j == 'X':
            if roman_string[i - 1] == 'I' and i != 0:
                sum -= 1
                sum += 9
            else:
                sum += 10
        elif j == 'L':
            if roman_string[i - 1] == 'X' and i != 0:
                sum -= 10
                sum += 40
            else:
                sum += 50
        elif j == 'C':
            if roman_string[i - 1] == 'X' and i != 0:
                sum -= 10
                sum += 90
            else:
                sum += 100
        elif j == 'D':
            if roman_string[i - 1] == 'C' and i != 0:
                sum -= 100
                sum += 400
            else:
                sum += 500
        elif j == 'M':
            if roman_string[i - 1] == 'C' and i != 0:
                sum -= 100
                sum += 900
            else:
                sum += 1000
        i += 1
    return sum
