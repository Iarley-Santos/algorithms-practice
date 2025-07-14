#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    l = len(arr)
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    
    print(positive/l)
    print(negative/l)
    print(zero/l)

if __name__ == '__main__':

    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)
