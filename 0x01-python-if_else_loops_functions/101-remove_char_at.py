#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ''
    j = 0
    for i in str:
        if j == n:
            j += 1
            continue
        strcpy += i
        j += 1
    return strcpy
