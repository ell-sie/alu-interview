#!/usr/bin/python3
"""testing file"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly `n` H characters in a text file.
    The text editor can execute only two operations: Copy All and Paste.
    """
    if n <= 1:
        return 0
    number = 1
    copy = number
    operations = 0
    while number < n:
        if n % number == 0:
            copy = number
            number = 2* copy
            operations += 2
        else:
            number += copy
            operations += 1
    return operations
