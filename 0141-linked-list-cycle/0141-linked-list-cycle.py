# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # p=head
        # s=set()
        # while p is not None:
        #     if p in s:
        #         return True
        #     s.add(p)
        #     p =p.next
        # return False
        fast=slow=head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if slow is fast:
                return True

        return False