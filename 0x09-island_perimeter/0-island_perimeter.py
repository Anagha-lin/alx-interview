#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]): A 2D grid where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:  # Handle empty grid
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check down
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1
                    
    return perimeter

