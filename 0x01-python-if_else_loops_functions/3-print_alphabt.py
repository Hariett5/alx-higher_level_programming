#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) == 'm' or chr(a) == 'n':
        continue
    print(chr(a).format(a), end='')
