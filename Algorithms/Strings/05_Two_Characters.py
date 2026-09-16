#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    """
    Pick two characters from the string, delete everything else, and check 
    if the result is a perfect alternation like ababab or baba.
    Try every possible pair and keep the longest valid result.
    """
    
    distinct = list(set(s))
    res = 0
    
    for i in range(len(distinct)):
        for j in range(i + 1, len(distinct)):
            a = distinct[i]
            b = distinct[j]
            
            last = None
            valid = True
            length = 0
            
            # scan s
            for c in s:
                if c == a or c == b:
                    # adjadent pairs
                    if c == last:
                        valid = False
                        break
                    
                    length += 1
                    last = c
                        
            if valid:
                res = max(res, length)
                
    return res
                    
                    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
