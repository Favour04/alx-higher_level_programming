#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    i = 0
    j = (len(my_list) - 1)
    while i < len(my_list):
        print("{:d}".format(my_list[j]))
        j -= 1
        i += 1
