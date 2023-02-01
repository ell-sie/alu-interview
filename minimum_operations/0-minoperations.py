#!/usr/bin/python3
"""testing file"""


def minOperations(n):
    """ a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    """
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        operations += 1
        if i == n:
            return operations
        while i <= 2 * n:
            i *= 2
            operations += 1
    return 0
