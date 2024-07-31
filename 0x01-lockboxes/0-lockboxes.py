def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    
    # Set to track visited boxes
    visited = set()
    
    # Queue for BFS
    queue = [0]
    
    while queue:
        # Get the current box
        box = queue.pop(0)
        
        if box not in visited:
            # Mark the box as visited
            visited.add(box)
            
            # Add all the keys in the current box to the queue
            for key in boxes[box]:
                if key < n and key not in visited:
                    queue.append(key)
    
    # Check if all boxes have been visited
    return len(visited) == n

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected: False

