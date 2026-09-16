#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    count_a = Counter(s[:mid])
    count_b = Counter(s[mid:])
    
    res = 0
    
    for c in count_a:
        res += max(0, count_a[c] - count_b[c])
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
