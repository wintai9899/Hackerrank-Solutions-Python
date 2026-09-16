#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Solution: Iterate half of s and compare s[i] - s[len(s) - 1 - i]
# Space Complexity: O(1)
# Time Complexity: O(N)
def theLoveLetterMystery(s):
    """
    Key Insight: A palindrome must have s[i] == s[n-1-i] for every mirrored pair
    """
    res = 0
    
    for i in range(len(s) // 2):
        changes = abs(ord(s[i]) - ord(s[len(s) - 1 - i]))
        res += changes
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
