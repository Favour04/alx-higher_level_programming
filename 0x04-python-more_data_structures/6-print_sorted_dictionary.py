#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    for i, k in sorted(a_dictionary.items()):
        print("{}: {}".format(i, k))
