#!/usr/bin/python3
"""
    Generates a Pascal's Triangle with n rows.
    Returns:
        A list of lists representing the Pascal's Triangle with n rows.
    """
    
    
def pascal_triangle(n):
    """
    Arguments:
    n -- an integer representing the number
    of rows to generate
    Returns:
    A list of lists of integers representing
    Pascal's triangle with n rows.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
    
