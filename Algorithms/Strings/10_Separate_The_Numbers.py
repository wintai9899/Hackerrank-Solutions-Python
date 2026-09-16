#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)
    
    for length in range(1, n // 2 + 1):
        first_str = s[:length]
        
        if first_str[0] == '0':
            continue
        
        first_num = int(first_str)
        expected = first_num
        i = 0
        count = 0
        
        while i < n:
            expected_str = str(expected)
            if not s.startswith(expected_str, i):
                break
            i += len(expected_str)
            expected += 1
            count += 1
        
        if i == n and count >= 2:
            print(f"YES {first_num}")
            return
    
    print("NO")
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
