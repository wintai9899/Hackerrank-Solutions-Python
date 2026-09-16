import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Space Complexity: O(N)
# Time Complexity: O(N)
def funnyString(s):
    r = s[::-1]
    
    s = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    r = [abs(ord(r[i]) - ord(r[i + 1])) for i in range(len(r) - 1)]
    
    return "Funny" if s == r else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
