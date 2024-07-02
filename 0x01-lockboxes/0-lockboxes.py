#!/usr/bin/python3
"""This module provides a function to determine if all the boxes
   in a given list can be opened using keys found within the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of list of int): A list where each element is a list of keys
                                 contained in that box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key not in opened_boxes and new_key < len(boxes):
            opened_boxes.add(new_key)
            keys.update(boxes[new_key])

    return len(opened_boxes) == len(boxes)
