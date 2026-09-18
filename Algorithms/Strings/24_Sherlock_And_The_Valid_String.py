#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Solution: Count freq for each freq
# Space Complexity: O(N)
# Time Complexity: O(N)
def isValid(s):
    # Counts the frequency of each chars
    # eg. s = abccc
    # char_freq = {a:1, b:1, c:3}
    char_freq = Counter(s)
    # freq_count = {1:2, 3:1}
    freq_count = {}
    
    for char, freq in char_freq.items():
        freq_count[freq] = freq_count.get(freq, 0) + 1
    
    if len(freq_count) == 1:
        return "YES"
    
    # there are two frequencies
    if len(freq_count) == 2:
        (freq1, count1), (freq2, count2) = freq_count.items()
        
        # case1: One character appears once, all others appear same number of times
        # eg. aabbc -> remove c
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return "YES"
        
        # case2: One character appears one extra time compared to others
        # eg. aabbb -> {2:2, 3: 1}
        if (freq1 == freq2 + 1 and count1 == 1) or (freq2 == freq1 + 1 and count2 == 1):
            return "YES"
            
    return "NO"
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
