#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

# Solution: Two pointers + Greedy
# Space Complexity: O(N)
# Time Complexity: O(N)
def highestValuePalindrome(s, n, k):
    s = list(s)
    # Tracks if the position has already been changed
    changed = [False] * n
    l = 0
    r = n - 1
    
    # Pass one: Make s a palindrome with minimal changes
    while l < r:
        if s[l] != s[r]:
            # make them equal
            if s[l] < s[r]:
                s[l] = s[r]
                
            else:
                s[r] = s[l]
            
            # mark l as changed
            changed[l] = True
            k -= 1
            
        l += 1
        r -= 1
        
    if k < 0:
        return '-1'
        
    # Pass Two: Maximize the palindrome since we still have k > 0, leftmost first
    l = 0
    r = n - 1
    
    while l < r:
        if s[l] != '9':
            # Already paid 1 change here in pass 1 only 1 more needed
            if changed[l]:
                if k >= 1:
                    s[l] = s[r] = '9'
                    k -= 1
            else:
            # Never touched - need 2 changes (both sides)
                if k >= 2:
                    s[l] = s[r] = '9'
                    k -= 2
        l += 1
        r -= 1
        
    # Odd length - middle digit is free to change with 1 cost
    if n % 2 == 1 and k >= 1:
        s[n // 2] = '9'
        
    return "".join(s)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
