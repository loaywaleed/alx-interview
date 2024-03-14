#!/usr/bin/python3
"""
Script that checks if all boxes can be unlocked
"""

boxes_1 = [[1], [2], [3], [4], []]
boxes_2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
boxes_3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]


def canUnlockAll(boxes):
    state_of_boxes = [True] # true is unlocked, false is locked
    unchecked = [] # checked means opened and checked
    for item in range(1, len(boxes)):
        state_of_boxes.append(False)

    for i in range(0, len(boxes)):
        if state_of_boxes[i] == True:
            for key in boxes[i]:
                state_of_boxes[key] = True
                for j in range(0, len(unchecked)):
                    if key == unchecked[j]:
                        for key in boxes[unchecked[j]]:
                            state_of_boxes[key] = True
        else:
            unchecked.append(i)

    for i in state_of_boxes:
        if i == False:
            return False
    return True

# if a box was closed before then check whats in it

print(canUnlockAll(boxes_1))
print(canUnlockAll(boxes_2))
print(canUnlockAll(boxes_3))
