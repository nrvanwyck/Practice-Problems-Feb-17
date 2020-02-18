# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

# For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

# Constraints

# For  of the test cases, .
# Output Format

# Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    full_repetitions = (n // len(s))
    leftover_characters = (n % len(s))
    a_count = 0
    for char in s:
        if char == 'a':
            a_count += 1
    leftover_a_count = 0
    for char in s[:leftover_characters]:
        if char == 'a':
            leftover_a_count += 1
    return ((full_repetitions * a_count) + leftover_a_count)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
