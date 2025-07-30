#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    lenght = len(s)
    cont = 0
    for i in range(lenght - m + 1):
        sum_total = 0
        for j in range(i, i+m):
            sum_total += s[j]
        if sum_total == d:
            cont += 1
    return cont

if __name__ == '__main__':

    s = [2, 2, 1, 3, 2]

    d = 4

    m = 2

    result = birthday(s, d, m)