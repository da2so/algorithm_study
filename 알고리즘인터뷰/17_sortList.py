#Given the head of a linked list, return the list after sorting it in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
from typing import  List
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

a1 = ListNode(4)
a2 = ListNode(1)
a3 = ListNode(2)
a4 = ListNode(3)

a1.next = a2
a2.next = a3
a3.next = a4
sol = Solution()
print(sol.sortList(a1))
