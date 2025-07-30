#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maximum = scores[0]
    cont_max = 0
    minimum = scores[0]
    cont_min = 0
    for i in scores:
        if i > maximum:
            cont_max += 1
            maximum = i
        elif i < minimum:
            cont_min += 1
            minimum = i
    return [cont_max, cont_min]
    
if __name__ == '__main__':
   
    scores = [12, 24, 10, 24]
    result = breakingRecords(scores)
