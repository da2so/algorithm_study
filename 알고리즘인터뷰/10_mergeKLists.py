
from typing import List
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next = None
import heapq
def mergeKLists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        result.next = node[1]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, result.next))

    return root.next

a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)

c1 = ListNode(2)
c2 = ListNode(6)

a1.next = a2
a2.next = a3

b1.next = b2
b2.next = b3

c1.next = c2

lists = [a1, b1, c1]
c = mergeKLists(lists)

while c is not None:
    print(c.val)
    c = c.next