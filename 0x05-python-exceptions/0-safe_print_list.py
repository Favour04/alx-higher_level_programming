#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    xchecker = 0
    if my_list is None:
        return 0

    for i in my_list:
        if xchecker == x:
            break
        try:
            print("{:d}".format(i), end='')
            count += 1
        except ValueError:
            continue
        xchecker += 1
    print("{}".format(''))
    return count
