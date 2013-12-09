from math import sqrt
import sys

for a in range(400):
    for b in range(400):
        c = sqrt(a**2 + b**2)
        if c == int(c):
            if a + b + c == 1000:
                print a*b*c
                sys.exit()
