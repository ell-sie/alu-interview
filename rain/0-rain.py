#!/usr/bin/python3
"""Calculate the amount of water retained by a set of walls.

    Args:
        walls (list of int): A list of non-negative integers representing the heights of walls
                             with unit width 1.

    Returns:
        int: The total amount of water retained in square units.

    Assumptions:
        - The ends of the list (before index 0 and after index walls[-1]) are not walls,
          meaning they will not retain water.
        - If the list is empty, the function returns 0.
    """
def rain(walls):
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Calculate the maximum heights of walls to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])

    # Calculate the maximum heights of walls to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    # Calculate the amount of water retained by each wall
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]

    return water
