#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            str1 += chr(ord(i) - 32)
        else:
            str1 += i
    print(str1)
