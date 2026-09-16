#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Solution: Two pointer
# Space Complexity: O(1)
# Time Complexity: O(N)
def hackerrankInString(s):
    i = 0
    j = 0
    
    while j < len("hackerrank") and i < len(s):
        if s[i] == "hackerrank"[j]:
            j += 1
        i += 1
        
    return "YES" if j == len("hackerrank") else "NO"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
