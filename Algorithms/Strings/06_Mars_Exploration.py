#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Solution: Iterate and compare with "SOS"[i % 3]
# Space Complexity: O(1)
# Time Complexity: O(N)
def marsExploration(s):
    # Write your code here
    res = 0
    
    for i in range(len(s)):
        if s[i] != "SOS"[i % 3]:
            res += 1
            
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()