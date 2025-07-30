#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    cont = 0
    max_val = max(candles)
    for i in candles:
        if i == max_val:
            cont += 1
    return cont

if __name__ == '__main__':
    
    candles = [1, 2, 4, 3, 4]

    result = birthdayCakeCandles(candles)
    print(result)
