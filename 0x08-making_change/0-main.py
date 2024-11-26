#!/usr/bin/python3
""" Main file for testing """

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 4
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
print(makeChange([7], 0))  # Output: 0
print(makeChange([5, 10], 7))  # Output: -1
print(makeChange([1, 5, 10, 25], 30))  # Output: 2 (25 + 5)

