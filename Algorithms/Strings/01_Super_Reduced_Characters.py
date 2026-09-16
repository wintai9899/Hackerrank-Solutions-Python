#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Solution: Stack
# Space Complexity: O(N)
# Time Complexity: O(N)
def superReducedString(s):
    stack = []
    
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            
        else:
            stack.append(c)
            
    return 'Empty String' if not stack else "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
