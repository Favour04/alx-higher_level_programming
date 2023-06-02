#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    if my_list is None:
        return 0

    while i < x:
        temp = my_list[i]
        try:
            print("{:d}".format(temp), end='')
            count += 1
            i += 1
        except ValueError:
            i += 1
        except TypeError:
            i += 1
    print("{}".format(''))
    return count
