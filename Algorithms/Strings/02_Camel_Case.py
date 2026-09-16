#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Solution: Count upper and add 1
# Space Complexity: O(1)
# Time Complexity: O(N)
def camelcase(s):
    upper = 0
    
    for c in s:
        if c.isupper():
            upper += 1
            
    return upper + 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')