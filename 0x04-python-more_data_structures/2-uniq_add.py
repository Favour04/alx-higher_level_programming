#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Create a set to store unique integers
    total = sum(unique_numbers)  # Calculate the sum of the unique integers
    return total
