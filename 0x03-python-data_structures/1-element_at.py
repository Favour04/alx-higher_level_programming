#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    i = 0
    while i < (len(my_list) + 1):
        if idx > len(my_list):
            return None
        elif i == idx:
            return my_list[i]
        i += 1
