#!/usr/bin/python3
"""Island Perimeter module"""


def island_perimeter(grid):
    """
    function that returns the perimeter of the island described in grid

    Args:
        grid: a list of list of integers.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
