#!/usr/bin/python3
def islower(c):
    tempc = ord(c)
    if tempc > 96 and tempc < 123:
        return True
    else:
        return False
