#!/usr/bin/python3
for i in range(0, 100):
    if i <= 9:
        print("{:02d},".format(i), end=" ")
    if i == 99:
        print("{:02d}".format(i))
    if i > 9:
        print("{:02d},".format(i), end=" ")
