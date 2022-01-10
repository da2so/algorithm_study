from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    root =  head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum+carry, 10)
        head.next = ListNode(val)
        head = head.next
    return root.next


a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)

a1.next = a2
a2.next = a3

b1.next = b2
b2.next = b3

c = addTwoNumbers(a1, b1)

while c is not None:
    print(c.val)
    c = c.next