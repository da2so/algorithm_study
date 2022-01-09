from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(val=4)

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

a1.next = a2
a2.next = a3
b1.next = b2
b2.next = b3

c = mergeTwoLists(a1, b1)

while c is not None:
    print(c.val)
    c = c.next