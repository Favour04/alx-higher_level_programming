#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    listcpy = my_list.copy()
    for i in my_list:
        a = i
        j = 0
        for i in listcpy:
            if a < i:
                break
            else:
                j += 1
        if j == len(listcpy):
            return a
