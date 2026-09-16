#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# Solution: Same logic as Anagram
# Space Complexity: O(s1 + s2)
# Time Complexity: O(s1 + s2)
def makingAnagrams(s1, s2):
    count_a = Counter(s1)
    count_b = Counter(s2)
    
    res = 0
    
    for char in set(s1) | set(s2):
        res += abs(count_a[char] - count_b[char])
        
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
