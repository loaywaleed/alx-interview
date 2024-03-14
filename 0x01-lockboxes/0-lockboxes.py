#!/usr/bin/python3
"""
Script that checks if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """Function that checks if we can unlock all the boxes"""
    state_of_boxes = [True]
    unchecked = []
    for item in range(1, len(boxes)):
        state_of_boxes.append(False)

    for i in range(0, len(boxes)):
        if state_of_boxes[i] is True:
            for key in boxes[i]:
                try:
                    tate_of_boxes[key] = True
                except:
                    pass
                for j in range(0, len(unchecked)):
                    if key == unchecked[j]:
                        for key in boxes[unchecked[j]]:
                            state_of_boxes[key] = True
        else:
            unchecked.append(i)

    for i in state_of_boxes:
        if i is False:
            return False
    return True
