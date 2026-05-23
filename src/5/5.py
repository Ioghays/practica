#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    return "YES" if (x2 - x1) % (v1 - v2) == 0 and (v1 > v2) else "NO"


x1, v1, x2, v2 = map(int, input().split())
print(kangaroo(x1, v1, x2, v2))