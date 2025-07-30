#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app = 0
    ora = 0
    for i in apples:
        if (i + a) >= s and (i + a) <= t:
            app += 1
    for i in oranges:
        if (i + b) >= s and (i + b) <= t:
            ora += 1
    print(app)
    print(ora)

if __name__ == '__main__':
    
    countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5 -6])
