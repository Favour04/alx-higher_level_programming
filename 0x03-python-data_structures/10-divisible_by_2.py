#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    boollist = my_list.copy()
    j = 0
    for i in my_list:
        if (i % 2) == 0:
            boollist[j] = True
            j += 1
        else:
            boollist[j] = False
            j += 1
    return (boollist)
