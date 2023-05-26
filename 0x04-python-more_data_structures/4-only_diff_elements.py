#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    for i in set_1:
        if i not in set_2:
            my_list.append(i)
    for i in set_2:
        if i not in set_1:
            my_list.append(i)
    return my_list
