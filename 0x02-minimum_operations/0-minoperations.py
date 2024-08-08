#!/usr/bin/python3
"""
Python3 challenge for calculating Minimum Operations.
For ALX_interview
"""

def minOperations(n):
    """
    Determines the minimum number of operations required to achieve exactly n 'H' characters in a file.
    If n cannot be reached, it returns 0.
    """
    if n <= 1:
        return 0

    pasted_chars = 1  # Number of characters in the file initially
    clipboard = 0  # Number of characters copied to the clipboard
    operations = 0  # Count of operations performed

    while pasted_chars < n:
        if clipboard == 0:  # Nothing copied yet
            clipboard = pasted_chars  # Copy all current characters
            operations += 1  # Increment operations for copy

        if pasted_chars == 1:  # Only one character in the file
            pasted_chars += clipboard  # Paste the copied characters
            operations += 1  # Increment operations for paste
            continue

        remaining = n - pasted_chars  # Characters needed to reach n
        if remaining < clipboard:  # Impossible if clipboard has more than needed
            return 0

        if remaining % pasted_chars != 0:  # If not divisible
            pasted_chars += clipboard  # Paste current clipboard contents
            operations += 1  # Increment operations for paste
        else:
            clipboard = pasted_chars  # Copy all current characters
            pasted_chars += clipboard  # Paste the copied characters
            operations += 2  # Increment operations for copy and paste

    return operations if pasted_chars == n else 0  # Return operations if n is reached

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of characters: "))
    print("Minimum number of operations to reach {} characters: {}".format(n, minOperations(n)))

