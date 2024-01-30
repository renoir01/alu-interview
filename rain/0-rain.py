#!/usr/bin/python3

"""
rain module
"""

def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    :param walls: List of non-negative integers representing the heights of walls.
    :return: Integer indicating the total amount of rainwater retained.
    """
    n = len(walls)

    if n <= 2:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(1, n - 1):
        min_height = min(left_max[i], right_max[i])
        if min_height > walls[i]:
            total_water += min_height - walls[i]

    return total_water

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6

    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))  # Output: 6

