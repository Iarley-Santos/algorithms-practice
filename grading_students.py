#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    mult_five = 0
    lenght = len(grades)
    for i in range(lenght):
        mult_five = ((grades[i] // 5) + 1) * 5
        if mult_five - grades[i] < 3 and grades[i] >= 38:
            grades[i] = mult_five
    return grades 

if __name__ == '__main__':
    
    grades = [73, 67, 38, 33]
    print(gradingStudents(grades))