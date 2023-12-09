#!/usr/bin/python3
for i in range(8):
    for j in range(i + 1, 9):
        print('{}{}, '.format(i, j), end='')
print('{}{}'.format(8, 9))
