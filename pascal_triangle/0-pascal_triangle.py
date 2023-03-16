#!/usr/bin/python3
"""
    Generates a Pascal's Triangle with n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        A list of lists representing the Pascal's Triangle with n rows.
    """
class Solution:
    def generate(self, numRows):
        triangles = []
        for i in range(numRows):
            triangles.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    triangles[i].append(1)
                else:
                    triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
        return
