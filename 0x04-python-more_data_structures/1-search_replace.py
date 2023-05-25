#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return my_list
    temp = []
    for i in my_list:
        if i == search:
            temp.append(replace)
        else:
            temp.append(i)
    return temp
