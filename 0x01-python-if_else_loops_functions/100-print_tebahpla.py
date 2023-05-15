#!/usr/bin/python3
for i in range(1,27):
    if i % 2 == 0:
        print("{}".format(chr((i * -1) + (123 - 32))), end='')
    else:
        print("{}".format(chr((i * -1) + 123)), end='')
