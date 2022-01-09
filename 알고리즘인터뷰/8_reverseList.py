
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next = None


def reverseList(l1: ListNode) -> ListNode:

    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev

        next, node.next = node.next, prev

        return reverse(next, node)

    return reverse(l1)


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)


a1.next = a2
a2.next = a3


c = reverseList(a1)

while c is not None:
    print(c.val)
    c = c.next