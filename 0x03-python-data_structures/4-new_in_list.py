#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    i = 0
    while i < (len(my_list)):
        if i == idx:
            my_listcpy = my_list.copy()
            my_listcpy[i] = element
            return my_listcpy
        i += 1
