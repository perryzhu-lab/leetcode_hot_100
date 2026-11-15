from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, p1, p2):
        dummy = ListNode(0)
        q = dummy
        q1 = p1
        q2 = p2
        while q1 is not None and q2 is not None:
            if q1.val <= q2.val:
                q.next = q1
                q1 = q1.next
            else:
                q.next = q2
                q2 = q2.next
            q = q.next

        if q1 is not None:
            q.next = q1
        if q2 is not None:
            q.next = q2

        return dummy.next

    def sortList(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)
