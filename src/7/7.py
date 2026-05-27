#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_breaks = 0
    min_breaks = 0

    for s in scores[1:]:
        if s > max_score:
            max_score = s
            max_breaks += 1
        elif s < min_score:
            min_score = s
            min_breaks += 1

    return [max_breaks, min_breaks]


if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().split()))

    result = breakingRecords(scores)

    print(result[0], result[1])