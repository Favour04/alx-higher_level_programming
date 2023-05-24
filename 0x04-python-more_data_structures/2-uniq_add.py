#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 1
    i = 0
    while i < len(my_list) - 2:
        if my_list[i] != my_list[n]:
            if i == 0:
               sums = my_list[i] + my_list[n]
            sums += my_list[n]
        n += 1
        i += 1
    return sums
