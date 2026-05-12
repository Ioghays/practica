#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []

    for grade in grades:
        if grade >= 38:
            next_multiple = ((grade // 5) + 1) * 5

            if next_multiple - grade < 3:
                grade = next_multiple

        result.append(grade)

    return result


n = int(input())
grades = []

for _ in range(n):
    grades.append(int(input()))

result = gradingStudents(grades)

for grade in result:
    print(grade)