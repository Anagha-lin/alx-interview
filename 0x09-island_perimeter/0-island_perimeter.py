#!/usr/bin/python3
"""
Module that contains the function to calculate the perimeter of an island
described in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): 2D grid where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over every cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is land
            if grid[i][j] == 1:
                # Start with 4 sides contributing to the perimeter
                perimeter += 4
                
                # Check the cell above (if it's in bounds and is land)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                
                # Check the cell below (if it's in bounds and is land)
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                
                # Check the cell to the left (if it's in bounds and is land)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                
                # Check the cell to the right (if it's in bounds and is land)
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    
    return perimeter

