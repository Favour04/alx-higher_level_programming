#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    i = idx + 1
    temp = my_list[:idx]
    temp += my_list[i:]
    my_list.clear()
    for i in temp:
        my_list.append(i)
    return my_list
