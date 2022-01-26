
from typing import List

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(array: List[int])-> List[int]:
    if not array:
        return None
    array = array.sort()
    mid = len(array) //2

    node = TreeNode(array[mid])
    node.left = sortedArrayToBST(array[:mid])
    node.right = sortedArrayToBST(array[mid+1:])
    return node

array = [-10, -3, 0, 5, 9]

