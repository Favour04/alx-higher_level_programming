#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    
    # Fist_name & Last_name must be a string 
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    
    if not isinstance(last_name, str):
        raise TypeError('first_name must be a string')

    #First_name or last_name must be given
    if first_name is None and last_name is None:
        raise ValueError('Missing argument')
    elif last_name is None and first_name:
        last_name = ' '

    print("My Name is {} {}".format(first_name, last_name))
