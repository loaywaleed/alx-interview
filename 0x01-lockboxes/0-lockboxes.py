#!/usr/bin/python3
"""
Script that checks if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """Function that checks if we can unlock all the boxes using BFS"""
    visited = set()
    queue = [0]
    while queue:
        current_box = queue.pop(0)
        if current_box not in visited:
            for key in boxes[current_box]:
                if key < len(boxes):
                    queue.append(key)
            visited.add(current_box)
    return len(boxes) == len(visited)
