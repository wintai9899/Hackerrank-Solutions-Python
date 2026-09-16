#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Solution: Counter and check for even and odd occurances
# Space Complexity: O(N)
# Time Complexity: O(N)
def gameOfThrones(s):
    count = Counter(s)
    for c in s:
        if count[c] > 1:
            # If char has even occurrances, we can use all of them
            if count[c] % 2 == 0:
                count[c] = 0
                
            else:
            # else, we have 1 left over
            # eg. "aabaaa" -> we can only use 4 "a"s
                count[c] = 1
    
    total_odds = sum(cnt for cnt in count.values())
    return "YES" if total_odds <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
