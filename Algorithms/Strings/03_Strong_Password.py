

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

# Solution: Counting
# Space Complexity: O(1)
# Time Complexity: O(N)
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
        
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    required_digit = 1
    required_lower = 1
    required_upper = 1
    required_special = 1
    
    for c in password:
        if c in numbers:
            required_digit = 0
            
        elif c in lower_case:
            required_lower = 0
            
        elif c in upper_case:
            required_upper = 0
            
        elif c in special_characters:
            required_special = 0
            
    missing_required = required_digit + required_lower + required_upper + required_special
    
    if n + missing_required < 6:
        return 6 - n
        
    return missing_required
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()