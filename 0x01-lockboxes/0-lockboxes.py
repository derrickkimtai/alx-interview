#!/usr/bin/python3
def canUnlockAll(boxes):
    """well documented"""
    if not boxes:
        return False

    n = len(boxes)
    unlocked_boxes = [False] * n
    unlocked_boxes[0] = True

    for i in range(n):
        if unlocked_boxes[i]:
            for key in boxes[i]:
                if 0 <= key < n:
                    unlocked_boxes[key] = True

    return all(unlocked_boxes)

