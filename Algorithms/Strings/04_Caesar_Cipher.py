#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# Solution: Helper method to encrypt using ord and chr
# Space Complexity: O(N)
# Time Complexity: O(N)
def caesarCipher(s, k):
    # Write your code here
    res = []
    k %= 26
    for c in s:
        res.append(shiftAlphabet(ord(c), k))
        
    return "".join(res)
    
def shiftAlphabet(c, k):
    # lower case
    if 97 <= c <= 122:
        c += k
        # wrap around
        if c > 122:
            c -= 26
        elif c < 97:
            c += 26
            
    # upper case
    if 65 <= c <= 90:
        c += k
        if c > 90:
            c -= 26
            
        elif c < 65:
            c += 26
            
    return chr(c)
    
    
    # upper case
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
