#!/usr/bin/python3
"""
Module to determine if all lockboxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from the first box.

    Args:
        boxes (list of list of int): A list where each element is a list of keys contained in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])
    
    while keys:
        key = keys.pop()
        if key not in opened_boxes and 0 <= key < n:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == n

