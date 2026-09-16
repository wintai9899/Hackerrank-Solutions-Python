#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Solution: Two Pointers
# Space Complexity: O(1)
# Time Complexity: O(N)
def palindromeIndex(s):
    """
    If s[i] == s[j], move both inward.

    If they differ, you must remove either s[i] or s[j]. Try removing each and check if the remaining substring is a palindrome:

    If removing s[i] works → return i.

    Else if removing s[j] works → return j.

    Else → -1
    """
    
    l = 0
    r = len(s) - 1
    
    while l <= r:
        if s[l] != s[r]:
            if isPalindrome(l + 1, r, s):
                return l
            if isPalindrome(l, r - 1, s):
                return r
        l += 1
        r -= 1
        
    return -1
    
def isPalindrome(l, r, s):
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
