#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    for i in argv:
        if i == argv[0]:
            j += 1
            continue
        else:
            print("{}: {}".format(j, argv[j]))
            j += 1
