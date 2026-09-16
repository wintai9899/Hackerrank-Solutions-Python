#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

# Solution: use set to store weights
# Space Complexity: O(N)
# Time Complexity: O(N)
def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    prev = None
    count = 0
    
    for c in s:
        if c == prev:
            count += 1
            
        else:
            prev = c
            count = 1
        # ord('a') = 97, but 1-indexed for weights so 96
        weight = (ord(c) - 96) * count
        weights.add(weight)
        
    res = ["Yes"] * len(queries)
    
    for i in range(len(queries)):
        if queries[i] not in weights:
            res[i] = "No"
            
    return res
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()