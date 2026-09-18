#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7
MAXN = 10**5 + 5

# Precompute factorials and inverse factorials once
fact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * MAXN
inv_fact[MAXN - 1] = pow(fact[MAXN - 1], MOD - 2, MOD)
for i in range(MAXN - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# Global prefix table built by initialize()
_prefix = []


def initialize(s):
    global _prefix
    n = len(s)
    _prefix = [[0] * 26 for _ in range(n + 1)]
    for i, ch in enumerate(s):
        row = _prefix[i + 1]
        prev = _prefix[i]
        for c in range(26):
            row[c] = prev[c]
        row[ord(ch) - 97] += 1


def answerQuery(l, r):
    pl = _prefix[l - 1]
    pr = _prefix[r]

    h = 0
    odd = 0
    denom_inv = 1

    for c in range(26):
        cnt = pr[c] - pl[c]
        half = cnt >> 1
        h += half
        if cnt & 1:
            odd += 1
        denom_inv = denom_inv * inv_fact[half] % MOD

    ways = fact[h] * denom_inv % MOD
    return ways * (odd if odd else 1) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
