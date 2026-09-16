#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

# Solution: Greedy -> Flip the last digit and skip the past
# Space Complexity: O(N)
# Time Complexity: O(N)
def beautifulBinaryString(b):
    res = 0
    b = list(b)
    i = 0
    
    while i < len(b) - 2:
        if b[i] == "0" and b[i + 1] == "1" and b[i + 2] == "0":
            # Flip the last char and skip
            b[i + 2] = 1
            res += 1
            i += 3
        else:
            i += 1
            
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
