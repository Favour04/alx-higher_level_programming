#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    print("{} arguments:".format(len(argv) - 1))
    for i in argv:
        if i == argv[0]:
            j += 1
            continue
        else:
            print("{}: {}".format(j, argv[j]))
            j += 1
