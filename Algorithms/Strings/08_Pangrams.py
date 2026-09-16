#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Solution: Counter
# Space Complexity: O(N) where N = 26 (if all distinct)
# Time Complexity: O(N)
def pangrams(s):
    letters = Counter(c.lower() for c in s if c.isalnum())
    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
