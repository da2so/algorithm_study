from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next = None

def swapPairs(l1: ListNode) -> ListNode:
    if l1 and l1.next:
        p = l1.next
        l1.next = swapPairs(p.next)
        p.next = l1
        return p
    return l1
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

a1.next = a2
a2.next = a3
a3.next = a4



c = swapPairs(a1)

while c is not None:
    print(c.val)
    c = c.next