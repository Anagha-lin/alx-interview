#!/usr/bin/python3
"""
This module contains a function to rotate a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A 2D matrix to rotate.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (convert rows into columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve 90-degree rotation
    for i in range(n):
        matrix[i].reverse()

