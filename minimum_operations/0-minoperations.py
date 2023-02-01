#!/usr/bin/python3
"""testing file"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly `n` H characters in a text file.
    The text editor can execute only two operations: Copy All and Paste.
    Arguments:
    n -- An integer representing the desired number of H characters
    Returns:
    An integer representing the fewest number of operations
    needed to achieve `n` H characters
    If `n` is impossible to achieve, return 0
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
