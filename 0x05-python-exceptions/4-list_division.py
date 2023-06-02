#!/usr/bin/pyhton3
def list_division(my_list_1, my_list_2, list_length):
    lists = []
    results = 0
    count = 0
    while count < list_length:
        try:
            results = my_list_1[count] / my_list_2[count]
        except TypeError:
            results = 0
            print("wrong type")
        except ZeroDivisionError:
            results = 0
            print("division by 0")
        except IndexError:
            results = 0
            print("out of range")
        finally:
            lists.append(results)
        count += 1
    return lists
