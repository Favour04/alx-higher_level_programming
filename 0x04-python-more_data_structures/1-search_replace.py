#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp = []
    for i in my_list:
        if i == search:
            temp.append(replace)
        else:
            temp.append(i)
    return temp
