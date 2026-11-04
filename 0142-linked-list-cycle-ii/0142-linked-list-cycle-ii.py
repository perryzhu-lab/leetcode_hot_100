# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = set()
        p = head
        while p is not None:
            if p in s:
                return p
            s.add(p)
            p = p.next
        return None
