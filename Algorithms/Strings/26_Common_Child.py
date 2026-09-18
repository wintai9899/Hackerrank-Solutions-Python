#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# Solution: DP
# Space Complexity: O(m * n)
# Time Complexity: O(m * n)
def commonChild(s1, s2):
    "Find the Longest Common Subsequence"
    dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    
    for i in range(len(s1) -1, -1, -1):
        for j in range(len(s2) -1, -1, -1):
            # If the characters match, we include this character in the LCS and move both pointers forward:
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
            # If characters don't match, we have two options:
            # 1. Skip character in text1: dp[i+1][j]
            # 2. Skip character in text2: dp[i][j+1]

            # We take the maximum because we want the longest subsequence.
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                
    return dp[0][0]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
