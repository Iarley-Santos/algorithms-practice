#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lenght = len(arr)
    main_diagonal = 0
    second_diagonal = 0
    for i in range(0, lenght):
        main_diagonal = main_diagonal + arr[i][i]
        second_diagonal = second_diagonal + arr[i][lenght-1-i]
    return abs(main_diagonal - second_diagonal)
        
if __name__ == '__main__':
    
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    print(diagonalDifference(arr))
