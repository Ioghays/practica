#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    count = 0

    for x in range(max(a), min(b) + 1):

        for i in a:
            if x % i != 0:
                break
        else:
            for i in b:
                if i % x != 0:
                    break
            else:
                count += 1

    return count


n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = getTotalX(a, b)

print(result)