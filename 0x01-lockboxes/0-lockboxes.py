#!/usr/bin/python3
def canUnlockAll(boxes):
    """this is he lock boxes code"""
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True

    for i in range(len(boxes)):
        if unlocked_boxes[i]:
            for key in boxes[i]:
                if key < len(boxes):
                    unlocked_boxes[key] = True

    return all(unlocked_boxes)

