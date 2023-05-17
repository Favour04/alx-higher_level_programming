#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(0)
    elif len(argv) == 2:
        sums = int(argv[1])
        print(sums)
    else:
        sums = int(argv[1])
        i = 0
        j = 2
        while i < (len(argv) - 2):
            sums += int(argv[j])
            i += 1
            j += 1
        print(sums)
