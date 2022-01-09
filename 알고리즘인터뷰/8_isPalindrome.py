from collections import deque
from typing import Deque

def isPalindrome(head) -> bool:
    q: Deque = deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True

