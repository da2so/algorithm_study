#연결리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성, 공간 복잡도 O(1), 시간 복잡도 O(n)

from dataclasses import dataclass
@dataclass
class ListNode:
    val: int
    next = None

def oddEventList(l1: ListNode) -> ListNode:
    if l1 is None:
        return None

    odd = l1
    even = l1.next
    even_haed = l1.next

    while even and even.next:
        even.next, odd.next = even.next.next, odd.next.next
        even, odd = even.next, odd.next
    odd.next = even_haed
    return l1

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5


c = oddEventList(a1)

while c is not None:
    print(c.val)
    c = c.next