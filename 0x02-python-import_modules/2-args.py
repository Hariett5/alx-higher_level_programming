#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if (nargs == 0):
        print("{:m} arguments.".format(nargs))
    elif (nargs == 1):
        print("{:m} argument:".format(nargs))
    else:
        print("{:m} arguments:".format(nargs))
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        print("{:m}: {:s}".format(str, sys.argv[str]))
